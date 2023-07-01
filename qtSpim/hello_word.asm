.data
hello_msg: .asciiz "Hello, World\n"
.text
.globl main
main:
li $v0, 4              # syscall code for print_string
la $a0, hello_msg      # load address of hello_msg into $a0
syscall                # make the system call
li $v0, 10             # syscall code for exit
syscall                # make the system call

