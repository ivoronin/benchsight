using System;

namespace cpu2006_import
{
    class Program
    {
        static void Main(string[] args)
        {
            var process = System.Diagnostics.Process.Start(@"D:\home\site\wwwroot\env\Scripts\python.exe", @"D:\home\site\wwwroot\manage.py cpu2006_import --delay 0.01");
            process.WaitForExit();
        }
    }
}
