#include <bits/stdc++.h>
#define int long long
using namespace std;

int gcd(int a, int b)
{
	//cout << b << " " << a%b <<endl;
	return b > 0 ? gcd(b, a%b): a;
}

signed main(){
	int a, b, c, d, v, q, w, e;
	cin >> a >> b>> c >> d >> v;
	q = d*v-b; w = a-c*v; e = gcd(abs(q), abs(w));
	if(q == 0 && w == 0) cout << "MULTIPLE";
	else if(w == 0) cout << "NONE";
	else
	{
		q /= e; w /= e;
		if(w < 0)
		{
			w = -w;
			q = -q;
		}
		cout << "X = " << q << '/' << w;
	}
}
