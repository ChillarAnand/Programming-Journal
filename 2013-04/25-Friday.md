# Update git on ubuntu from command line
`sudo apt-get install python-software-properties <br>
sudo add-apt-repository ppa:git-core/ppa <br>
sudo apt-get update <br>
sudo apt-get install git <br> ` 


# git User configuration
git config --global user.name "username"
git config --global user.email "your.email@gmail.com" 
 

#git - color highlighting for console 
git config --global color.ui true
git config --global color.status auto
git config --global color.branch auto 


# set vim as default editor for Git (Linux)
git config --global core.editor vim 


# query git settings of local repo
git config --list 


#push changes to git
push add origin

#find the size of git repository
git bundle create tmp.bundle --all
du -sh tmp.bundle
#to count hooks, stashes, config, rerere cache, backups 
git gc
du -sh .git/

# store git credentials
git config credential.helper store
git push http://example.com/repo.git

# where is git installed
which git
