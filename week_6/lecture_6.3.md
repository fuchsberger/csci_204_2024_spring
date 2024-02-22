## Useful Git Commands

#### Setting up public key authentication (unix system)
```bash
cd ~
ssh-keygen
```
Hit `Enter` three times when asked stuff.

Then go to [https://gitlab.bucknell.edu](https://gitlab.bucknell.edu). Login and go to Preferences -> SSH Keys

Add your public key as a new key. You can find your public key using the following command:
```bash
cat ~/.ssh/id_rsa.pub
```

This is a one time thing and allows you to use gitlab without ever entering your password again.

#### Setup/copy a repository for the first time
```bash
git clone <link_to_git.git>
```

#### Upload To Repository
```bash
git add . && git commit -m "<msg>"
git push
```
Carefull. Do not change the same files at the same time! --> Git Conflict. This is going to be a disaster to resolve.


#### Download from Repository
```bash
git pull
```

#### Collaboration using Git

To collaborate on a project one team member should create a repository in Gitlab and invite the other team members as `Maintainers`.

You can then all clone the repository, push and pull to it.

