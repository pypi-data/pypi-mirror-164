# dash_cm

## Install
```bash
pip install --upgrade dash_cm
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


## Make '.model' file executable

Create the two following files:


- `/usr/share/mime/packages/cardiac-model.xml`
    ```
    <?xml version="1.0" encoding="UTF-8"?>
        <mime-info xmlns="https://www.freedesktop.org/standards/shared-mime-info">
        <mime-type type="application/zip">
            <comment xml:lang="en">Cardiac Model</comment>
            <glob pattern="*.model"/>
            <glob pattern="*.zip"/>
        </mime-type>
    </mime-info>
    ```

- `/usr/share/applications/cardiac-model.desktop`
    ```
    [Desktop Entry]
    Encoding=UTF-8
    Version=1.0
    Type=Application
    Terminal=true
    Exec=dashcm load %F
    Name=CardiacModel
    Icon=<path-to>/dash_cm/build/static/icons/logo_512.png
    ```
