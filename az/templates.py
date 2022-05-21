@staticmethod
class Templates():
    template_code_snippet = '''@CODE@'''
    template_unity_script = '''using UnityEngine;
using System.Collections;
using Oskar.Core;

namespace @NAMESPACE@
{
    public class @CLASS@ : @INHERITANCE@
    {
        @CODE@
    }
}
    '''
    template_console_app = '''using System;
    namespace @NAMESPACE@
    {
        class @CLASS@
        {
            internal class Program
            {
                @CODE@
            }
        }
    }'''