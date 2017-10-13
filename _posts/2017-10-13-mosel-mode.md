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
  nil ;; handled below
  '("model" "end-model" "uses" "declarations" "end-declarations" "maximise" "minimise" "writeln" "XPRS_OPT" "XPRS_UNF" "XPRS_INF" "XPRS_UNB" "XPRS_OTH" "case" "end-case" "forall" "sum" "in" "array" "of") ;; keywords
  '(
	("(!.*?\\(\n.*?\\)*?!)" . 'font-lock-comment-face) ;; the RE is right but it seems to fail for blocks longer than a few lines
	("!.*?$" . 'font-lock-comment-face)
	(";" . 'font-lock-builtin)
	(":=" . 'font-lock-builtin)
	("::" . 'font-lock-builtin)
	("\\.\\." . 'font-lock-builtin)
	("<=" . 'font-lock-builtin)
	(">=" . 'font-lock-builtin)
	("=" . 'font-lock-builtin)
	(":" . 'font-lock-builtin)
	("linctr" . 'font-lock-function-name-face)
	("mpvar" . 'font-lock-function-name-face)
	("real" . 'font-lock-function-name-face)
	("integer" . 'font-lock-function-name-face)
	("string" . 'font-lock-function-name-face)
	("end-procedure" . 'font-lock-function-name-face)
	("procedure" . 'font-lock-function-name-face)
	("end-function" . 'font-lock-function-name-face)
	("function" . 'font-lock-function-name-face)
    )
  '("\\.mos\\'") ;; filename suffix
  nil ;; extra function hooks
  "Major mode for Mosel highlighting.")

{% endhighlight %}

Installation
------------

Paste it into your `.emacs` file and execute it with `C-x C-e`. When
you edit a `.mos` file, it will automatically go into `mosel-mode`.
