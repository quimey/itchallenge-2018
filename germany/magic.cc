#include<iostream>

#define forn(i, n) for(int i=0; i < (int) n; i++)


using namespace std;

int t[5][5];


bool check(int d) {
	forn(i, 5) {
		int s = 0;
		forn(j, 5) s += t[i][j];
		if(s != d) return false;
	}
	forn(i, 5) {
		int s = 0;
		forn(j, 5) s += t[j][i];
		if(s != d) return false;
	}
	int s = 0;
	forn(i, 5) s += t[i][i];
	if(s != d) return false;
	s = 0;
	forn(i, 5) s += t[i][4 - i];
	if(s != d) return false;
	return true;
}

int bt(int i, int j) {
	if (i == 5) {
		int d = 0;
		forn(k, 5) d += t[0][k];
		//forn(a, 5) {forn(b, 5)cout << t[a][b];} cout << endl << endl;
		return (int) check(d);
	}
	if (j == 5) {
		if(i) {
			int d = 0, e = 0;
			forn(k, 5) d += t[0][k];
			forn(k, 5) e += t[i][k];
			if (d != e) return 0;
		}
		return bt(i + 1, 0);
	}
	int res = 0;
	if (i == 0) cout << i << " " << j << endl;
	forn(k, 4) {
		t[i][j] = k;
		if(i == 4) {
			int d = 0, e = 0;
			forn(l, 5) d += t[0][l];
			forn(l, 4) e += t[l][j];
			if(d != e + k) continue;
		}
		res += bt(i, j + 1);
	}
	return res;
}

int main() {
	forn(i, 5) forn(j, 5) t[i][i] = -1;
	cout << bt(0, 0) << endl;
}
