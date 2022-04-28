// File utilities

// File read
string file_read(string file) => System.IO.File.ReadAllText(@file);

// File search
string[] file_search(string file) => System.IO.Directory.GetFiles(path, file);

// File create
void file_create(string file) => System.IO.File.Create(@file);

// File delete
void file_delete(string file) => System.IO.File.Delete(@file);

// Directory create
string directory_create(string directory) => System.IO.Directory.CreateDirectory(@directory);

// Directory delete
void directory_delete(string directory) => System.IO.Directory.Delete(@directory);

// compile_knot
void knot_compile(string arg) => System.Diagnostics.Process.Start("trans.py", arg);

// // Compiler types
// err -> string[]
// List<string> err = new List<string>();

// // temp err
// err -> void

// // Build
// build -> main -> to C# entry point for Console Application
