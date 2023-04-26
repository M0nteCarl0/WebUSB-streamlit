import pandas as pd
import streamlit as st

html_code = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>WebUSB Example</title>
    <script>
        async function connect() {
            const device = await navigator.usb.requestDevice({ filters: [{ vendorId: 0x2B3E }] });
            console.log(device);
        }
    </script>
</head>
<body>
    <button onclick="connect()">Connect to USB device</button>
</body>
</html>
"""

st.components.v1.html(html_code)












