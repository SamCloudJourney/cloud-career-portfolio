from pathlib import Path
import sys

if len(sys.argv) != 2:
    raise SystemExit("usage: patch_roslyn_regression.py <roslyn-root>")

root = Path(sys.argv[1])
p = root / "src/Compilers/Server/VBCSCompilerTests/AnalyzerConsistencyCheckerTests.cs"
s = p.read_text(encoding="utf-8-sig")

marker = """        /// <summary>
        /// A differing MVID is okay when it's loading a DLL from the compiler directory.
"""

test = r'''
        [Fact]
        public void SameMvidDifferentContentSameDirectory_CurrentMainAcceptsCollision()
        {
            var directory = Temp.CreateDirectory();
            var assemblyLoader = AnalyzerAssemblyLoader.CreateNonLockingLoader(directory.CreateDirectory("resolver").Path);

            var key = NetStandard20.References.netstandard.GetAssemblyIdentity().PublicKey;
            var analyzer = CreateNetStandardDll(
                directory,
                "MvidCollision",
                "1.0.0.0",
                key,
                "public static class Marker { public const string Value = \"TRUSTED\"; }");

            var analyzerReferences = ImmutableArray.Create(
                new CommandLineAnalyzerReference(analyzer.Path));

            Assert.True(AnalyzerConsistencyChecker.Check(
                directory.Path,
                analyzerReferences,
                assemblyLoader,
                Logger));

            var originalMvid = AssemblyUtilities.ReadMvid(analyzer.Path);
            var originalBytes = File.ReadAllBytes(analyzer.Path);
            var originalHash = Convert.ToHexString(
                System.Security.Cryptography.SHA256.HashData(originalBytes));

            using (var stream = new FileStream(analyzer.Path, FileMode.Append, FileAccess.Write, FileShare.ReadWrite))
            {
                stream.Write(Encoding.UTF8.GetBytes("ATTACKER_CONTROLLED_DIFFERENT_CONTENT_20260921"));
            }

            var changedMvid = AssemblyUtilities.ReadMvid(analyzer.Path);
            var changedBytes = File.ReadAllBytes(analyzer.Path);
            var changedHash = Convert.ToHexString(
                System.Security.Cryptography.SHA256.HashData(changedBytes));

            Assert.Equal(originalMvid, changedMvid);
            Assert.NotEqual(originalHash, changedHash);

            var result = AnalyzerConsistencyChecker.Check(
                directory.Path,
                analyzerReferences,
                assemblyLoader,
                Logger,
                out List<string>? errorMessages);

            Console.WriteLine($"CURRENT_MAIN_ORIGINAL_MVID={originalMvid}");
            Console.WriteLine($"CURRENT_MAIN_CHANGED_MVID={changedMvid}");
            Console.WriteLine($"CURRENT_MAIN_ORIGINAL_SHA256={originalHash}");
            Console.WriteLine($"CURRENT_MAIN_CHANGED_SHA256={changedHash}");
            Console.WriteLine($"CURRENT_MAIN_MVID_EQUAL={originalMvid == changedMvid}");
            Console.WriteLine($"CURRENT_MAIN_CONTENT_HASH_DIFFERENT={originalHash != changedHash}");
            Console.WriteLine($"CURRENT_MAIN_CHECK_RESULT={result}");

            Assert.True(result);
            Assert.Null(errorMessages);
        }

'''

if "SameMvidDifferentContentSameDirectory_CurrentMainAcceptsCollision" in s:
    raise SystemExit("test already exists unexpectedly")
if marker not in s:
    raise SystemExit("insertion marker not found")

p.write_text(s.replace(marker, test + marker), encoding="utf-8")
print(p)
