#include <bits/std++.h>

using ll = long long;

// Don't you love floating point precision?
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int s, r;

    std::cin >> s >> r;
    double a = s*s, b = 3.14159*r*r;
    std::cout << (a < b ? "CIRCLE" : "SQUARE");
}