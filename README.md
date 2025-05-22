<h1>💻 IoT System Monitoring with AWS</h1>

<p><strong>Author:</strong> Anowar Uddin</p>
<p><strong>GitHub:</strong> <a href="https://github.com/a-uddin/IoT-system-monitoring" target="_blank">https://github.com/a-uddin/IoT-system-monitoring</a></p>

<h2>📌 Project Overview</h2>
<p>
  This project demonstrates a complete IoT system that collects and monitors real-time device metrics using AWS services. 
  A Python script runs on a local device (e.g., laptop or Raspberry Pi), captures system statistics, and publishes them via MQTT to AWS IoT Core. 
  The data is then routed to Amazon Timestream through an IoT Rule and visualized in real-time using Amazon Managed Grafana.
</p>

<h2>🧱 Architecture</h2>
<ul>
  <li>IoT Device runs Python script to collect system metrics</li>
  <li>MQTT protocol used to publish messages securely to AWS IoT Core</li>
  <li>AWS IoT Rule forwards messages to Amazon Timestream using IAM role</li>
  <li>Grafana dashboard visualizes Timestream data</li>
</ul>

<h3>🔗 Technologies Used</h3>
<ul>
  <li><strong>Python</strong> (psutil, paho-mqtt)</li>
  <li><strong>AWS IoT Core</strong></li>
  <li><strong>Amazon Timestream</strong></li>
  <li><strong>Amazon Managed Grafana</strong></li>
  <li><strong>AWS IAM</strong> (for secure role-based access)</li>
</ul>

<h2>📂 Files in This Repository</h2>
<ul>
  <li><code>laptop_stats.py</code> – Collects CPU, memory, disk, and network stats</li>
  <li><code>send_to_aws.py</code> – Connects to AWS IoT Core via MQTT and publishes metrics</li>
  <li><code>.gitignore</code> – Prevents uploading local certs/keys or config files</li>
  <li><code>README.md</code> – Project documentation (you are reading it!)</li>
</ul>

<h2>📈 Use Case</h2>
<p>
  This setup is ideal for learning or demonstrating:
</p>
<ul>
  <li>IoT data flow in AWS</li>
  <li>Secure MQTT messaging</li>
  <li>Real-time system monitoring</li>
  <li>Cloud-native dashboarding with Grafana</li>
</ul>

<h2>🔒 Security Notes</h2>
<p>
  Certificate/key paths and AWS endpoint have been removed or replaced with placeholders to protect sensitive data. 
  Always use <code>.gitignore</code> to avoid pushing credentials.
</p>

<h2>📌 Diagram</h2>
<p>
  <img src="https://github.com/a-uddin/IoT-system-monitoring/blob/main/IoT-Architecture.png" width="600">
</p>

<h2>📬 Contact</h2>
<p>
  Connect on LinkedIn or reach out for collaboration and opportunities.<br>
  <strong>Email:</strong> smanowar.uddin@gmail.com<br>
  <strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/anowar-uddin" target="_blank">anowar-uddin</a>
</p>
