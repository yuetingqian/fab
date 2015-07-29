# fab
#### install requirements
pip install -r requirements

#### usage

Modify `env.hosts` and `env.user` in `fabfile.py` .

Then run command to add user with `sudo` authority:

`fab add_user:name=cara,group=sudo`
