//#include <stdio.h>

#define BOYUT 8

int main() {
    char tahta[BOYUT][BOYUT];

    // Tahtayı başlangıç dizilimine ayarlama
    for (int i = 0; i < BOYUT; i++) {
        for (int j = 0; j < BOYUT; j++) {
            if (i == 0 || i == 7) {  // Siyah ve beyaz taşlar
                if (j == 0 || j == 7) {
                    tahta[i][j] = (i == 0) ? 'r' : 'R';  // Kale
                } else if (j == 1 || j == 6) {
                    tahta[i][j] = (i == 0) ? 'n' : 'N';  // At
                } else if (j == 2 || j == 5) {
                    tahta[i][j] = (i == 0) ? 'b' : 'B';  // Fil
                } else if (j == 3) {
                    tahta[i][j] = (i == 0) ? 'q' : 'Q';  // Vezir
                } else if (j == 4) {
                    tahta[i][j] = (i == 0) ? 'k' : 'K';  // Şah
                }
            } else if (i == 1) {
                tahta[i][j] = 'p';  // Siyah piyonlar
            } else if (i == 6) {
                tahta[i][j] = 'P';  // Beyaz piyonlar
            } else {
                tahta[i][j] = '.';  // Boş kareler
            }
        }
    }

    // Tahtayı yazdırma
    for (int i = 0; i < BOYUT; i++) {
        for (int j = 0; j < BOYUT; j++) {
            printf("%c ", tahta[i][j]);
        }
        printf("\n");
    }

    return 0;
}

