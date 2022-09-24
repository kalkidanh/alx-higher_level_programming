	.file	"10-check_cycle.c"
	.text
	.globl	check_cycle
	.type	check_cycle, @function
check_cycle:
.LFB6:
	.cfi_startproc
	endbr64
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movq	%rdi, -24(%rbp)
	movq	-24(%rbp), %rax
	movq	%rax, -16(%rbp)
	movq	-24(%rbp), %rax
	movq	%rax, -8(%rbp)
	jmp	.L2
.L11:
	movq	-24(%rbp), %rax
	movq	8(%rax), %rax
	movq	%rax, -24(%rbp)
	movq	-16(%rbp), %rax
	movq	8(%rax), %rax
	movq	8(%rax), %rax
	movq	%rax, -16(%rbp)
	movq	-24(%rbp), %rax
	cmpq	-16(%rbp), %rax
	jne	.L2
	movq	-8(%rbp), %rax
	movq	%rax, -24(%rbp)
	movq	-16(%rbp), %rax
	movq	%rax, -8(%rbp)
.L8:
	movq	-8(%rbp), %rax
	movq	%rax, -16(%rbp)
	jmp	.L3
.L5:
	movq	-16(%rbp), %rax
	movq	8(%rax), %rax
	movq	%rax, -16(%rbp)
.L3:
	movq	-16(%rbp), %rax
	movq	8(%rax), %rax
	cmpq	%rax, -24(%rbp)
	je	.L4
	movq	-16(%rbp), %rax
	movq	8(%rax), %rax
	cmpq	%rax, -8(%rbp)
	jne	.L5
.L4:
	movq	-16(%rbp), %rax
	movq	8(%rax), %rax
	cmpq	%rax, -24(%rbp)
	je	.L13
	movq	-24(%rbp), %rax
	movq	8(%rax), %rax
	movq	%rax, -24(%rbp)
	jmp	.L8
.L13:
	nop
	movl	$1, %eax
	jmp	.L9
.L2:
	cmpq	$0, -24(%rbp)
	je	.L10
	cmpq	$0, -16(%rbp)
	je	.L10
	movq	-16(%rbp), %rax
	movq	8(%rax), %rax
	testq	%rax, %rax
	jne	.L11
.L10:
	movl	$0, %eax
.L9:
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE6:
	.size	check_cycle, .-check_cycle
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
