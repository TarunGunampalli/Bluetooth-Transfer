#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


^+D::
Run, bash,,,myBash
WinWaitActive, ahk_pid %myBash%
send cd /mnt/c/Users/tarun/Downloads {Enter}
Send python3 earbuds.py {Enter}
WinHide, ahk_pid %myBash%
Sleep, 5000
WinClose, ahk_pid %myBash%
return