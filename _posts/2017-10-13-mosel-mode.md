---
layout: post
title: mosel-mode
tags: code emacs
---

`mosel-mode`
========

Mosel is a language for defining LP and IP models, used by Xpress-MP
among other solvers. I couldn't find an Emacs mode for editing Mosel, so  here's a small contribution which does some syntax highlighting. It also lives at
[EmacsWiki](http://www.emacswiki.org/emacs/MoselMode).

{% highlight scheme %}

(define-generic-mode 'mosel-mode
  ;; comment characters
  '("!")
  '("model" "end-model" "uses" "declarations" "end-declarations" "writeln" "case" "end-case" "else" "in" "array" "of" "getsol" "getsensrng" "getobjval" "is_integer") ;; keywords
  '(
	("(!.*?\\(\n.*?\\)*?!)" . 'font-lock-comment-face) ;; the RE is right but it seems to fail for blocks longer than a few lines
	(";" . 'font-lock-builtin-face)
	(":=" . 'font-lock-builtin-face)
	("::" . 'font-lock-builtin-face)
	("\\.\\." . 'font-lock-builtin-face)
	("<=" . 'font-lock-builtin-face)
	(">=" . 'font-lock-builtin-face)
	("=" . 'font-lock-builtin-face)
	(":" . 'font-lock-builtin-face)
	("linctr" . 'font-lock-function-name-face)
	("mpvar" . 'font-lock-function-name-face)
	("real" . 'font-lock-function-name-face)
	("integer" . 'font-lock-function-name-face)
	("string" . 'font-lock-function-name-face)
	("sum" . 'font-lock-function-name-face)
	("forall" . 'font-lock-function-name-face)
	("end-procedure" . 'font-lock-function-name-face)
	("procedure" . 'font-lock-function-name-face)
	("end-function" . 'font-lock-function-name-face)
	("function" . 'font-lock-function-name-face)
	("maximize" . 'font-lock-function-name-face)
	("minimize" . 'font-lock-function-name-face)
	("XPRS_OPT" . 'font-lock-constant-face)
	("XPRS_UNF" . 'font-lock-constant-face)
	("XPRS_INF" . 'font-lock-constant-face)
	("XPRS_UNB" . 'font-lock-constant-face)
	("XPRS_OTH" . 'font-lock-constant-face)
    )
  '("\\.mos\\'") ;; filename suffix
  nil ;; extra function hooks
  "Major mode for Mosel highlighting.")

{% endhighlight %}

Installation
------------

Paste it into your `.emacs` file and execute it with `C-x C-e`. When
you edit a `.mos` file, it will automatically go into `mosel-mode`.
