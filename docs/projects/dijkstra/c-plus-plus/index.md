---
title: Dijkstra in C++
layout: default
date: 2022-10-06
featured-image: dijkstra-in-every-language.jpg
last-modified: 2022-10-06

---

Welcome to the [Dijkstra](https://sampleprograms.io/projects/dijkstra) in [C++](https://sampleprograms.io/languages/c-plus-plus) page! Here, you'll find the source code for this program as well as a description of how the program works.

## Current Solution

{% raw %}

```c++
#include <bits/stdc++.h>
#define pii pair<int, int>
using namespace std;

const int N = 7;
bool vis[N];
vector<pii> g[N];
vector<int> dis(N, INT_MAX);

void handle_error()
{
    cout << "Usage: please provide three inputs: a serialized matrix, a source node and a destination node";
    exit(0);
}

int check(string s)
{
    int x1 = 0, x2 = (int)s.size() - 1;

    for (int i = 0; i < s.size(); i++)
    {
        if (s[i] != ' ')
        {
            x1 = i;
            break;
        }
    }

    for (int i = (int)s.size() - 1; i >= x1; i--)
    {
        if (s[i] != ' ')
        {
            x2 = i;
            break;
        }
    }

    for (int i = x1; i <= x2; i++)
    {
        if (s[i] == ' ')
        {
            handle_error();
        }
    }

    return stoi(s);
}

vector<int> convert(string s)
{

    if (s.size() == 0)
    {
        handle_error();
    }
    vector<int> v;
    string num = "";
    for (int i = 0; i < s.size(); i++)
    {
        if (((int)s[i] >= 48 && (int)s[i] <= 57) || s[i] == ' ' || s[i] == '-')
        {
            num += s[i];
        }
        else if (s[i] == ',')
        {
            int x = check(num);
            if (x < 0)
                handle_error();
            v.push_back(x);
            num = "";
        }
    }

    if (num.size() > 0)
    {
        int x = check(num);
        if (x < 0)
            handle_error();
        v.push_back(x);
    }

    return v;
}

vector<int> dijkstra(int src)
{
    set<pii> s;
    s.insert({dis[src], src});
    while (!s.empty())
    {
        pii tp = *s.begin();
        int tpn = tp.second, tpd = tp.first;
        s.erase({tpd, tpn});
        for (auto it : g[tpn])
        {
            int chd = it.second;
            int chn = it.first;
            if (tpd + chd < dis[chn])
            {
                auto it = s.find({dis[chn], chn});
                if (it != s.end())
                    s.erase(it);
                dis[chn] = tpd + chd;
                s.insert({dis[chn], chn});
            }
        }
    }
    return dis;
}

int main(int argc, char *argv[])
{

    if (argc <= 1)
        handle_error();
    vector<int> bin = convert(argv[1]), nodes = convert(argv[2]), t = convert(argv[3]);
    if (bin.size() == 0 || nodes.size() == 0 || t.size() == 0)
        handle_error();
    int des = t[0];
    int src = nodes[0];
    if (src < 0 || des < 0)
        handle_error();

    int sz = sqrt((int)bin.size());
    if (sz * sz != bin.size())
        handle_error();
    int k = 0;
    for (int i = 0; i < bin.size(); i += sz)
    {
        for (int j = i; j < i + sz; j++)
        {
            if (bin[j] < 0)
                handle_error();
            if (bin[j] != 0)
            {
                g[j - sz * k].push_back({k, bin[j]});
                g[k].push_back({j - sz * k, bin[j]});
            }
        }
        k++;
    }

    dis[src] = 0;
    vector<int> ans = dijkstra(src);
    if (dis[des] == INT_MAX)
        handle_error();
    cout << ans[des] << "\n";
}
```

{% endraw %}

[Dijkstra](https://sampleprograms.io/projects/dijkstra) in [C++](https://sampleprograms.io/languages/c-plus-plus) was written by:

- Ajay Maheshwari
- Jeremy Grifski

If you see anything you'd like to change or update, [please consider contributing](https://github.com/TheRenegadeCoder/sample-programs).

**Note**: The solution shown above is the current solution in the Sample Programs repository as of Oct 10 2022 16:05:09. The solution was first committed on Oct 06 2022 05:18:52. As a result, documentation below may be outdated.

## How to Implement the Solution

No 'How to Implement the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).

## How to Run the Solution

No 'How to Run the Solution' section available. [Please consider contributing](https://github.com/TheRenegadeCoder/sample-programs-website).