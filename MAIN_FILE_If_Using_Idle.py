import imp
import tkinter
import beta1
import homepage
if __name__=='__main__':
    imp.reload(homepage)
    while True:
        imp.reload(beta1)
        beta1.main()
        if beta1.reset_val==1:
            continue
        if beta1.exit_val==1:
            break     
