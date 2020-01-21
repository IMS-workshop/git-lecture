# git

## Warm-Up
- how to start a repo from scratch? 
    - `git init` local method
    - on GitHub `git clone` and either `git push --force` or `git pull` methods
- how to revert mistakes?
    - `git revert` vs. …
    - `git reset` vs. …
    - `git reset --hard` vs. …
    - `git restore`
- how to go to a specific point in history?
    - `git checkout SHA` ⟶ `DETACHED HEAD` problem
    - interaction with branches
- `git gui`: building commits along the way interactively (for the *mess around* type of workflows)

## The Open Source model
- remotes: `pull`, `push`, `fetch`, `merge`
- GitHub: forks, branches and PRs
- strategies for keeping your fork up-to-date: your `master` and upstream's `master`, short-lived and long-lived topic branches
- a more thorough and deailed explanation can be found on the [Numpy Contributor's Guide](https://docs.scipy.org/doc/numpy/dev/gitwash/index.html). This guide can be adapted to your own needs, see [gitwash](https://github.com/matthew-brett/gitwash).

### Installing Git GUI

If you encounter something like `git gui is not a git command` then probably Git GUI isn't installed yet. You can add it to your Git installation in the following ways:

#### macOS
```
# If this command outputs something with "AppleGit" you have a slimmed down version of Git
git --version
# In that case, continue with the following commands

# 1. Download the official installer from https://git-scm.com/download/mac and install it
...

# 2. Create an alias in .bash_profile
# Add a line "alias git='/usr/local/git/bin/git'" (without the ""), then save and exit
nano ~/.bash_profile

# 3. Activate the current configuration
source ~/.bash_profile

# 4. Test the change
git gui
```

#### Ubuntu
```
# Use the following command to add Git GUI to your installation
sudo apt install git-gui

# If you do a fresh Git install, you could also use this command to get everything at once
sudo apt install git-all
```

