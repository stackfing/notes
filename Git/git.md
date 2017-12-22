# 本地

`git init` 创建仓库

历史提交记录 `git log` 可在添加 `--pretty=oneline` 作为一行一行显示

恢复上一次提交 `git reset --hard HEAD^` 先查看历史提交分支 `git log` 上两条 HEAD^^ 上 n 条 HEAD~n 或者 `git reset --hard commit_id`

恢复上次分支再回到目前分支，先查看命令历史 `git reflog` 再使用 `git reset --hard reflog_id`

`git add` 将修改放在暂存区

`git commit` 将文件提交在分支上

`git checkout -- file` 文件改乱还未放在暂存区（未 git add)，恢复现在最新分支

`git reset HEAD file` 文件提交在暂存区（已 git add），恢复到未 add 之前，再 checkout

`git checkout -- file` 本地误删文件需要恢复

`git rm file` 确实需要删除工作区文件

# 远程

关联远程仓库 `git remote add origin git@github.com:username/learngit.git` 要将 ssh key 公钥放在账户列表中，关联好之后远程仓库名称是 origin

`git push origin master` 推送当前分支 master 到远程分支

推送本地分支到远程分支并且关联远程分支 `git push origin -u master`

`git rm --cached readme1.txt`    删除readme1.txt的跟踪，并保留在本地。

`git rm --f readme1.txt`    删除readme1.txt的跟踪，并且删除本地文件。



## 拉取分支

git fetch --all 拉取远程所有分支

git checkout 别人分支

git pull origin 别人分支

git checkout 自己分支

git merge --no-ff 别人分支

有冲突就解决 add commit 最后 push origin 自己分支

# 撤销修改

在工作区中作了修改，暂未提交在暂存区：`git checkout -- file` 

在工作区中作了修改，已经提交在暂存区：`git reset HEAD file` 将暂存区的撤销，重新放回工作区，然后 `git checkout -- file`

# 分支

创建分支 `git checkout -b dev` 创建 dev 分支并且切换到 dev 分支

查看当前分支 `git branch`

切换分支 `git checkout dev`

合并分支 先切换到 master 然后 `git merge dev`

# 冲突

master 有修改， dev 也有修改，在 `git merge dev` 时不可以快速合并，需要处理冲突

冲突处理完毕，`git add -A` 添加到暂存区然后提交，合并完成

查看分支合并图： `git log --graph`

