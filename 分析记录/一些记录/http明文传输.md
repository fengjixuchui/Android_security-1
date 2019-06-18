# http明文传输
## Breaking UC Browser
* Attack Vector
'''Manifest
<service android:exported="false" android:name="com.uc.deployment.UpgradeDeployService" android:process=":deploy" />
'''
when service launches
browser makes a POST to 'puds.ucweb.com/upgrade/index.xhtml' with http
response,browser receive a command to download any update or a new module.
but we noticed that when trying to open a PDF file in the browser, it repeats the request to the above address, then downloads a native library. 
PDF with native library for viewing PDF files.

1. POST to html
2. compressed library for viewing PDF files and office documents.
request and response is encrypted,but library is compressed in a ZIP file and not encrypted.

try and decrypt server's response.
look at com.uc.deployment.UpgradeDeployService class
from the onStartCommand method, we navigate to com.uc.deployment.b.x, and then to com.uc.browser.core.d.c.f.e:

'''
package com.taobao.wireless.security.adapter;
public class JNICLibrary {
    public static native Object doCommandNative(int arg0, Object[] arg1);
}
'''

Machine code obfuscation

节头表无效 libsgmainso-6.4.36.so

程序头表足够正确load ELF文件与分析了, simply delete the section header table.

这里发生了什么？乍一看，函数的开头和结尾是ARM体系结构的典型特征。第一条指令将函数将使用的寄存器的内容推送到堆栈（在本例中为R0，R1和R2），以及LR寄存器的内容和函数的返回地址。最后一条指令恢复保存的寄存器并将返回地址放入PC寄存器，从而从函数返回。但是如果我们仔细观察一下，我们可能会注意到倒数第二条指令改变了存储在堆栈中的返回地址。让我们计算代码执行时的内容。地址0xB130在R1中加载，从中减去5，然后移到R0并接收0x10的加法。最后，它等于0xB13B。因此，IDA认为最终指令执行正常的函数返回，而实际上，它执行到计算的地址0xB13B的传输。

现在让我们提醒您，ARM处理器有两种模式和两组指令 -  ARM和Thumb。地址的低位确定处理器将使用哪个指令集即地址实际为0xB13A，而低位的值表示Thumb模式。
类似的“适配器”和一些语义垃圾被添加到该库中每个函数的开头。但我们不会详细讨论它们。请记住，几乎所有功能的真正开始都是进一步的。

由于代码中没有显式转换为0xB13A，因此IDA无法识别那里有代码。出于同样的原因，它不会将库中的大多数代码识别为代码，这使得分析有点棘手。所以，我们告诉IDA有代码，这就是：

sub_494c

在LR寄存器中调用此函数时，我们得到上述表的地址（0xB144）。 R0包含此表中的索引。 也就是说，我们从表中获取值，将其添加到LR，并获取我们需要去的地址。 让我们尝试计算它：0xB144 + [0xB144 + 8 * 4] = 0xB144 + 0x120 = 0xB264。 我们导航到这个地址并看到一些有用的指令，然后转到0xB140：

现在将在偏移处转换为表中的索引0x20。
根据表的大小来判断，代码中会有很多这样的转换。 因此，我们希望自动处理此问题，避免手动计算地址。 因此，脚本和在IDA中修补代码的能力来解救我们：

