#include <bits/stdc++.h>
using namespace std;

float findMin(float data[], int n){
    float xMin = data[0];
    for (int i = 0 ; i<n; i++){
        if (xMin > data[i]) {xMin = data[i];}
    }

    return xMin;
}


float findMax(float data[], int n){
    float xMax = data[0];
    for (int i = 0 ; i<n; i++){
        if (xMax < data[i]) {xMax = data[i];}
    }

    return xMax;
}

// Hàm nhận mảng dưới dạng cú pháp mảng
void dataStd_SimpleScaling(float data[], int n, float xMax) {
    float x=0;

    cout << "Simple Scaling" << endl;
    for (int i = 0; i < n; ++i) {
        x = data[i] / xMax;
        cout << x << "    ";
    }
    cout << endl;
}

void dataStd_MinMaxScaling(float data[], int n, float xMax, float xMin){
    float x = 0;
    
    cout << "Min-Max Scaling" << endl;
    for (int i = 0; i < n; ++i) {
        x = (data[i] - xMin) / (xMax - xMin);
        cout << x << "    ";
    }
    cout << endl;
}

void dataStd_ZScoreScaling (float data[], int n){
    // Mau phuong sai  n-1

    //Tinh Trung Binh
    float xTB = 0;
    for (int i=0; i<n; i++){
        xTB = xTB + data[i];
    }

    xTB = xTB / n;

    // Tinh Phuong Sai
    float xSD = 0;
    for (int i=0; i<n; i++){
        xSD = xSD + pow(data[i] - xTB,2);
    }

    xSD = sqrt((1.0/(n-1)) * xSD);

    // Tinh Z-Score
    float x = 0;
    cout << "Z-Scaling:" << endl;
    for (int i=0; i<n; i++){
        x = (data[i] - xTB) / xSD;
        cout << x << fixed << setprecision(2) << "    ";
    }

}

int main() {
    float data[] = {10, 20, 30, 40, 50};
    int n = sizeof(data) / sizeof(data[0]);

    float xMax = findMax(data, n);
    float xMin = findMin(data, n);
    dataStd_SimpleScaling(data, n, xMax);  // Truyền mảng vào hàm
    dataStd_MinMaxScaling(data, n, xMax, xMin);
    dataStd_ZScoreScaling(data, n);
    return 0;
}
