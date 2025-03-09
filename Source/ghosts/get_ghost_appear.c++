#include "iostream"
#include "fstream"
#include "string"
using namespace std;

int main() {
    ifstream fin("text.txt");

    string temp;
    getline(fin, temp);
    short len = temp.length();

    bool** matrix = new bool*[len];

    for (short i = 0; i < len; ++i) {
        matrix[i] = new bool[len];
        for (short j = 0; j < len; ++j)
            matrix[i][j] = temp[j] - '0';
        if (!fin.eof())
            getline(fin, temp);
    }

    fin.close();

    ofstream fout("output.txt");
    for (int i = 0; i < len; ++i) {
        fout << '[';

        for (int j = 0; j < len; ++j) {
            fout << matrix[i][j];
            if (j != len - 1)
                fout << ',';
        }

        fout << "],\n";
    }
    fout.close();

    for (short i = 0; i < len; ++i)
        delete[] matrix[i];
    delete[] matrix;
}