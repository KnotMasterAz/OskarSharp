using System.Collections.Generic;
using UnityEngine;

// README
// This file should be put on a gameobject which persists between scenes.
// It is used to register and unregister signals.
// Without this code, signals will not work.

namespace KnotsSharp
{
    class Signal : MonoBehaviour
    {
        // Instance of the signal
        public static Signal Instance;

        // Signal list
        private List<string> _signals;

        // Set the instance
        private void Awake()
        {
            SignalDestroyAll();
            instance = this;
        } 

        //unity_add_signal -> Signal.instance.AddSignal
        public void AddSignal(string channel, string signal) => _signals.Add(Signalify(channel, signal));

        //unity_remove_signal -> Signal.instance.RemoveSignal
        public void RemoveSignal(string channel, string signal) => _signals.Remove(Signalify(channel, signal));

        //unity_signal_destroy -> Signal.instance.DestroySignal
        public void SignalDestroyAll() => _signals = new List<string>();

        //unity_signal_exists -> Signal.instance.SignalExists
        public bool SignalExists(string channel, string signal) => _signals.Contains(Signalify(channel, signal));

        // Used to create a signal string (DO NOT USE THIS FUNCTION)
        private string Signalify(string channel, string signal) => ($"{channel}:{signal}");

    }
}