#include <iostream>
#include <cstdlib>
#include <ctime>
#include <string>
using namespace std;
int main()
{
    cout << "--------------------" << endl << "密碼生成器 Version 2.0_2022.04.02" << endl << "Made By YU KAI" << endl << "--------------------" << endl << endl;
    while(true)
    {
        int n;
        cout << "輸入密碼的長度:";
        cin >> n;
        srand(time(0));
        int groups;
        cout << "輸入生成幾組密碼:";
        cin >> groups;
        string alphanum("");
        string character[]={"0123456789","abcdefghijklmnopqrstuvwxyz","ABCDEFGHIJKLMNOPQRSTUVWXYZ","!@#$\%^&*"};
        string announcement[]={"是否要加入1-9？ [Y/N] ","是否要加入a-z？ [Y/N] ","是否要加入A-Z？ [Y/N] ","是否要加入「!@#$\%^&*」？ [Y/N] "};
        char answer;
        for(int j=0;j<4;j++)
        {
            cout << announcement[j];
            cin >> answer;
            if (answer == 'Y' or answer == 'y')
                alphanum += character[j];
        }
        cout << "是否要而外輸入字符？ [Y/N] ";
        cin >> answer;
        if (answer == 'Y' or answer == 'y')
        {
            string add;
            cout << "輸入而外字符:" << endl;
            cin >> add;
            alphanum += add;
        }
        int string_length = alphanum.length() -1;
        cout << "生成的密碼:" << endl;
        for (groups; groups>0; groups--)
        {
            for (int i = 0; i < n; i++)
                cout << alphanum[rand() % string_length];
            cout << endl;
        }
        cout << endl;
    }
    return 0;
}