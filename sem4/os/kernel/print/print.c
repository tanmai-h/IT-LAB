#include <linux/module.h>
#include <linux/kernel.h>

MODULE_LICENSE("GPL");   
MODULE_AUTHOR("tanmai"); 
MODULE_DESCRIPTION("printMe"); 
MODULE_VERSION("3.141592");

int init_module (void)
{
        printk ( "\nHello\n" );            
        return 0;
}
 
void cleanup_module (void)
{
        printk ( "\nBYE\n" );
}