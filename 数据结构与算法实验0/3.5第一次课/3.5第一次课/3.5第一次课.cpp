// 3.5第一次课.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include <iostream>
using namespace std;
#include <time.h>
int main()
{
//while循环求100累加
   /* int s=0,i=0;
    while (i <= 100) {
        s += i;
        i++;
    }
    cout << "s=" << s << endl;*/
//do...while循环求30阶乘
    /*float s = 1.0;
    int i = 1;
    do {
        s *= i;
        i++;
    } while (i <= 30);
    cout << s;*/
//1.车牌号问题：四位数，前俩数字一样，后俩数字一样，不为同一数字，且是某整数平方：
    /*int nx = 999;
    int na=0, nb=0,ns=0;
    for (nx; nx <= 9999; nx++) {
        int nc=0, nd=0,ne=0,nf=0;
        nc = nx % 10;//最后一位
        nd = nx / 10;//为求倒数第二位数做准备
        ne = nd % 10;//倒数第二位
        nf = nd / 10;//为求倒数第三位数做准备
        if (ne == nc) { int nm = 0, nn = 0, no = 0;
        nm = nf % 10;//倒数第三位
        nn = nf / 10;
        no = nn % 10;//倒数第四位
        if (nm == no && nm != ne)
        {   
            //ns = nx;
            //cout << ns << endl;//输出所有的满足前两个条件的数
            for (int ni = 31; ni < 100; ni++) {
                int nz = 0;
                nz = ni * ni;//循环平方，找相等
                if (nz == nx) {
                    cout << "车牌号是："<<nx <<","<<ni << endl;
                }
            }
        }
        }
    }*/
//2.随机抽取学号(1-30)
    /*srand((unsigned)time(NULL));
    int nc;
    do{
        int na = rand() % (30 - 1 + 1) + 1;
        cout << "按1开始进行抽取,按0结束！" << endl;
        cin >> nc;
        switch (nc) {
        case(1):
            cout << na << "\n" << "抽取结束" << endl;
            break;
        case(0):
            cout << "结束抽取，欢迎下次使用！" << endl;
            break;
        default:
            cout << "输入错误！" << endl;
            break;
        }
    } while (nc != 0);*/
//2(2)两个班
    /*srand((unsigned)time(NULL));
    int nc;
    do {
        int na = rand() % (216 - 101 + 1) + 101;
        cout << "按1开始进行抽取,按0结束！" << endl;
        cin >> nc;
        if (na > 115 && na < 201) {
            do {
                na = rand() % (216 - 101 + 1) + 101;
            } while (na > 115 && na < 201);
            switch (nc) {
            case(1):
                cout << na << "\n" << "抽取结束" << endl;
                break;
            case(0):
                cout << "结束抽取，欢迎下次使用！" << endl;
                break;
            default:
                cout << "输入错误！" << endl;
                break;
            }
        }
        else {
            switch (nc) {
            case(1):
                cout << na << "\n" << "抽取结束" << endl;
                break;
            case(0):
                cout << "结束抽取，欢迎下次使用！" << endl;
                break;
            default:
                cout << "输入错误！" << endl;
                break;
            }
        }
    } while (nc != 0); */

    std::cout << "Hello World!\n";
    return 0;
}

// 运行程序: Ctrl + F5 或调试 >“开始执行(不调试)”菜单
// 调试程序: F5 或调试 >“开始调试”菜单

// 入门使用技巧: 
//   1. 使用解决方案资源管理器窗口添加/管理文件
//   2. 使用团队资源管理器窗口连接到源代码管理
//   3. 使用输出窗口查看生成输出和其他消息
//   4. 使用错误列表窗口查看错误
//   5. 转到“项目”>“添加新项”以创建新的代码文件，或转到“项目”>“添加现有项”以将现有代码文件添加到项目
//   6. 将来，若要再次打开此项目，请转到“文件”>“打开”>“项目”并选择 .sln 文件
