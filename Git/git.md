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






## 拉取分支

git fetch --all 拉取远程所有分支

git checkout 别人分支

git pull origin 别人分支

git checkout 自己分支

git merge --no-ff 别人分支

有冲突就解决 add commit 最后 push origin 自己分支