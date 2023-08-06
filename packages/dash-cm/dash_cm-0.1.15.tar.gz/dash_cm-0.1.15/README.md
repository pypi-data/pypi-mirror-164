# dash_cm

## Install
```bash
pip install dash_cm
```

Optionally:
```bash
sudo tee /usr/local/bin/dashcm > /dev/null <<EOT
#!/usr/bin/bash

exec "python" -m dash_cm "\$@"
EOT
sudo chmod +x /usr/local/bin/dashcm
```

And then use as executable
```bash
dashcm serve &
```