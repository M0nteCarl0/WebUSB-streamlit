import pandas as pd
import streamlit as st

requset_devices = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>WebUSB Example</title>
    <script>
        async function connect() {
            const device = await navigator.usb.requestDevice({ filters: [{ deviceClass : 0x0 }] });
            alert(device);
        }
    </script>
</head>
<body>
    <button onclick="connect()">Connect to USB device</button>
</body>
</html>
"""


st.components.v1.html(requset_devices)












