# Study Abroad Maze

## By Tergel Myagmarsaikhan

## Theme
The path through a study abroad program. The whole sequence beginning to start all the way back home. Choose carefully.

## How to Solve
1. Unzip the study-abroad-office folder and enter the study-abroad-office directory
2. Windows/Powershell users: before doing anything else, run 
".\hide-dotfiles.ps1" from inside the study-abroad-office folder so hidden files behave correctly. If you hit a permissions error, run:

"Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass"

and then try

".\hide-dotfiles.ps1"

3. Now you can start the maze
4. Use ls and cd to explore, use cat to read clue files
5. Some directories are dead ends
6. One clue is hidden, you should try "ls -a" once you're in the right directory. Windows/PowerShell users: to see hidden files, use "Get-ChildItem -Force" instead of "ls -a"
7. Reach passport.txt to complete the maze

## Commands you'll need

ls, ls -a, Get-ChildItem -Force, cd, cat, cd ..