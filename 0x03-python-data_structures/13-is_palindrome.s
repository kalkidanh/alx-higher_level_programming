	.file	"13-is_palindrome.c"
	.text
	.globl	reverse
	.type	reverse, @function
reverse:
.LFB6:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movq	%rdi, -40(%rbp)
	movq	$0, -24(%rbp)
	movq	-40(%rbp), %rax
	movq	(%rax), %rax
	movq	%rax, -16(%rbp)
	jmp	.L2
.L3:
	movq	-16(%rbp), %rax
	movq	8(%rax), %rax
	movq	%rax, -8(%rbp)
	movq	-16(%rbp), %rax
	movq	-24(%rbp), %rdx
	movq	%rdx, 8(%rax)
	movq	-16(%rbp), %rax
	movq	%rax, -24(%rbp)
	movq	-8(%rbp), %rax
	movq	%rax, -16(%rbp)
.L2:
	cmpq	$0, -16(%rbp)
	jne	.L3
	movq	-40(%rbp), %rax
	movq	-24(%rbp), %rdx
	movq	%rdx, (%rax)
	nop
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE6:
	.size	reverse, .-reverse
	.globl	compare
	.type	compare, @function
compare:
.LFB7:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movq	%rdi, -24(%rbp)
	movq	%rsi, -32(%rbp)
	movq	-24(%rbp), %rax
	movq	%rax, -16(%rbp)
	movq	-32(%rbp), %rax
	movq	%rax, -8(%rbp)
	jmp	.L5
.L9:
	movq	-16(%rbp), %rax
	movl	(%rax), %edx
	movq	-8(%rbp), %rax
	movl	(%rax), %eax
	cmpl	%eax, %edx
	jne	.L6
	movq	-16(%rbp), %rax
	movq	8(%rax), %rax
	movq	%rax, -16(%rbp)
	movq	-8(%rbp), %rax
	movq	8(%rax), %rax
	movq	%rax, -8(%rbp)
	jmp	.L5
.L6:
	movl	$0, %eax
	jmp	.L7
.L5:
	cmpq	$0, -16(%rbp)
	je	.L8
	cmpq	$0, -8(%rbp)
	jne	.L9
.L8:
	cmpq	$0, -16(%rbp)
	jne	.L10
	cmpq	$0, -8(%rbp)
	jne	.L10
	movl	$1, %eax
	jmp	.L7
.L10:
	movl	$0, %eax
.L7:
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE7:
	.size	compare, .-compare
	.globl	is_palindrome
	.type	is_palindrome, @function
is_palindrome:
.LFB8:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$80, %rsp
	movq	%rdi, -72(%rbp)
	movq	%fs:40, %rax
	movq	%rax, -8(%rbp)
	xorl	%eax, %eax
	movq	-72(%rbp), %rax
	movq	(%rax), %rax
	movq	%rax, -24(%rbp)
	movq	-24(%rbp), %rax
	movq	%rax, -32(%rbp)
	movq	-32(%rbp), %rax
	movq	%rax, -40(%rbp)
	movq	$0, -16(%rbp)
	movl	$1, -52(%rbp)
	movq	-72(%rbp), %rax
	movq	(%rax), %rax
	testq	%rax, %rax
	je	.L12
	movq	-72(%rbp), %rax
	movq	(%rax), %rax
	movq	8(%rax), %rax
	testq	%rax, %rax
	je	.L12
	jmp	.L13
.L15:
	movq	-32(%rbp), %rax
	movq	8(%rax), %rax
	movq	8(%rax), %rax
	movq	%rax, -32(%rbp)
	movq	-40(%rbp), %rax
	movq	%rax, -24(%rbp)
	movq	-40(%rbp), %rax
	movq	8(%rax), %rax
	movq	%rax, -40(%rbp)
.L13:
	cmpq	$0, -32(%rbp)
	je	.L14
	movq	-32(%rbp), %rax
	movq	8(%rax), %rax
	testq	%rax, %rax
	jne	.L15
.L14:
	cmpq	$0, -32(%rbp)
	je	.L16
	movq	-40(%rbp), %rax
	movq	%rax, -16(%rbp)
	movq	-40(%rbp), %rax
	movq	8(%rax), %rax
	movq	%rax, -40(%rbp)
.L16:
	movq	-40(%rbp), %rax
	movq	%rax, -48(%rbp)
	movq	-24(%rbp), %rax
	movq	$0, 8(%rax)
	leaq	-48(%rbp), %rax
	movq	%rax, %rdi
	call	reverse
	movq	-48(%rbp), %rdx
	movq	-72(%rbp), %rax
	movq	(%rax), %rax
	movq	%rdx, %rsi
	movq	%rax, %rdi
	call	compare
	movl	%eax, -52(%rbp)
	cmpq	$0, -16(%rbp)
	je	.L17
	movq	-24(%rbp), %rax
	movq	-16(%rbp), %rdx
	movq	%rdx, 8(%rax)
	movq	-48(%rbp), %rdx
	movq	-16(%rbp), %rax
	movq	%rdx, 8(%rax)
	jmp	.L12
.L17:
	movq	-48(%rbp), %rdx
	movq	-24(%rbp), %rax
	movq	%rdx, 8(%rax)
.L12:
	movl	-52(%rbp), %eax
	movq	-8(%rbp), %rcx
	xorq	%fs:40, %rcx
	je	.L19
	call	__stack_chk_fail@PLT
.L19:
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE8:
	.size	is_palindrome, .-is_palindrome
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0"
	.section	.note.GNU-stack,"",@progbits
	.section	.note.gnu.property,"a"
	.align 8
	.long	 1f - 0f
	.long	 4f - 1f
	.long	 5
0:
	.string	 "GNU"
1:
	.align 8
	.long	 0xc0000002
	.long	 3f - 2f
2:
	.long	 0x3
3:
	.align 8
4:
