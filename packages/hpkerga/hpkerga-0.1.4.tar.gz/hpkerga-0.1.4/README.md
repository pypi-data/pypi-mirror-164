# hpkerga

`pip install hpkerga`

Go to https://hp.kerga.fr.

### Add a custom entry
```bash
python -m hpkerga GitLab \
    --url https://gitlab.com \
    --image https://about.gitlab.com/images/press/logo/png/gitlab-logo-500.png \
    --group Group_1
```

### Send the file
```bash
python -m hpkerga send
```