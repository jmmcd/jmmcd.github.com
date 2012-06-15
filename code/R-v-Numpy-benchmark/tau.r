cmd_args = commandArgs();
n = as.real(cmd_args[4]) # use like this: R --vanilla --silent < tau.r 10 [10 is then arg 4]
x <- runif(n*n, 0.0, 1.0)
y <- runif(n*n, 0.0, 1.0)
system.time(cor.test(x, y, method="kendall"))