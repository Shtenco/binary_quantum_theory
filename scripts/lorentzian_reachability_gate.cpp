#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <unordered_set>
#include <vector>
using namespace std;

using Spin=array<int,10>;
using Prof=array<int,10>;
static int edge_idx[5][5];
static vector<int> neigh[5];
static const array<pair<int,int>,10> edges={{{0,1},{0,2},{0,3},{0,4},{1,2},{1,3},{1,4},{2,3},{2,4},{3,4}}};

static int mult4(int a,int b,int c,int d){
    int lo1=abs(a-b),hi1=a+b,lo2=abs(c-d),hi2=c+d;
    if(((lo1-lo2)&1)) return 0;
    int lo=max(lo1,lo2),hi=min(hi1,hi2);
    if(((lo-lo1)&1)) ++lo;
    return lo<=hi ? (hi-lo)/2+1 : 0;
}
static long long gauss_mult(const Spin&s){
    long long p=1;
    for(int v=0;v<5;++v){
        int q[4],n=0;
        for(int w:neigh[v]) q[n++]=s[edge_idx[v][w]];
        int m=mult4(q[0],q[1],q[2],q[3]);
        if(!m) return 0;
        p*=m;
    }
    return p;
}
static uint64_t enc_spin(const Spin&s){
    uint64_t x=0;for(int i=0;i<10;++i)x|=((uint64_t)s[i])<<(4*i);return x;
}
static Spin dec_spin(uint64_t x){
    Spin s{};for(int i=0;i<10;++i)s[i]=(x>>(4*i))&15;return s;
}
static uint64_t enc_prof(const Prof&p){
    uint64_t x=0;for(int i=0;i<10;++i)x|=((uint64_t)p[i])<<(4*i);return x;
}
static Prof dec_prof(uint64_t x){
    Prof p{};for(int i=0;i<10;++i)p[i]=(x>>(4*i))&15;return p;
}
static Prof addp(const Prof&a,const Prof&b){
    Prof c{};for(int i=0;i<10;++i)c[i]=a[i]+b[i];return c;
}
static int E(int a,int b){return edge_idx[a][b];}

static vector<Prof> euclidean_profiles(int v){
    set<uint64_t> uniq;
    vector<int> ns=neigh[v];
    for(int a:ns)for(int b:ns)for(int c:ns){
        if(a==b||a==c||b==c)continue;
        Prof p{};
        p[E(v,a)]++;p[E(a,b)]++;p[E(v,b)]++;p[E(v,c)]+=2;
        uniq.insert(enc_prof(p));
    }
    vector<Prof> out;for(auto x:uniq)out.push_back(dec_prof(x));return out;
}
static vector<Prof> lorentzian_profiles(int v){
    auto he=euclidean_profiles(v);set<uint64_t> uniq;vector<int> ns=neigh[v];
    for(int i:ns)for(int j:ns)for(int k:ns){
        if(i==j||i==k||j==k)continue;
        for(const auto&p1:he)for(const auto&p2:he){
            Prof p=addp(p1,p2);
            p[E(v,i)]+=2; // h_i[h_i^-1,K]
            p[E(v,j)]+=2; // h_j[h_j^-1,K]
            p[E(v,k)]+=2; // h_k[h_k^-1,V]
            uniq.insert(enc_prof(p));
        }
    }
    vector<Prof> out;for(auto x:uniq)out.push_back(dec_prof(x));return out;
}
static vector<Prof> full_profiles(int v){
    set<uint64_t> u;for(auto&p:euclidean_profiles(v))u.insert(enc_prof(p));
    for(auto&p:lorentzian_profiles(v))u.insert(enc_prof(p));
    vector<Prof> o;for(auto x:u)o.push_back(dec_prof(x));return o;
}

static vector<int> final_vals(int s,int n){
    bool cur[20]={},nxt[20]={};cur[s]=true;
    for(int r=0;r<n;++r){
        fill(begin(nxt),end(nxt),false);
        for(int x=0;x<19;++x)if(cur[x]){if(x)nxt[x-1]=true;nxt[x+1]=true;}
        copy(begin(nxt),end(nxt),begin(cur));
    }
    vector<int> o;for(int x=0;x<20;++x)if(cur[x])o.push_back(x);return o;
}
static void dfs_reach(int e,Spin&cur,const array<vector<int>,10>&opts,unordered_set<uint64_t>&out){
    if(e==10){if(gauss_mult(cur))out.insert(enc_spin(cur));return;}
    for(int x:opts[e]){cur[e]=x;dfs_reach(e+1,cur,opts,out);}
}
static unordered_set<uint64_t> apply_support(const unordered_set<uint64_t>&inputs,const vector<Prof>&profiles){
    unordered_set<uint64_t> out;out.reserve(inputs.size()*16);
    for(auto code:inputs){
        Spin s=dec_spin(code);
        for(const auto&p:profiles){
            array<vector<int>,10> opts;
            for(int e=0;e<10;++e)opts[e]=final_vals(s[e],p[e]);
            Spin cur{};dfs_reach(0,cur,opts,out);
        }
    }
    return out;
}
static void block_stats(const unordered_set<uint64_t>&states,string label){
    set<uint64_t> quartets;map<int,long long> distinct_hist,occ_hist;
    long long dim=0;int maxs=0;
    for(auto x:states){
        Spin s=dec_spin(x);dim+=gauss_mult(s);for(int q:s)maxs=max(maxs,q);
        for(int v=0;v<5;++v){
            uint64_t c=0;int q[4],n=0;
            for(int w:neigh[v]){q[n]=s[E(v,w)];c|=((uint64_t)q[n])<<(4*n);++n;}
            quartets.insert(c);occ_hist[mult4(q[0],q[1],q[2],q[3])]++;
        }
    }
    for(auto c:quartets){int q[4];for(int n=0;n<4;++n)q[n]=(c>>(4*n))&15;distinct_hist[mult4(q[0],q[1],q[2],q[3])]++;}
    cout<<label<<" assignments="<<states.size()<<" dimension="<<dim<<" max_j="<<maxs/2.0<<" distinct_local_blocks="<<quartets.size()<<"\n";
    cout<<label<<" distinct_block_multiplicities";for(auto&kv:distinct_hist)cout<<" m"<<kv.first<<":"<<kv.second;cout<<"\n";
    cout<<label<<" occurrence_multiplicities";for(auto&kv:occ_hist)cout<<" m"<<kv.first<<":"<<kv.second;cout<<"\n";
}
int main(){
    for(int i=0;i<5;++i)for(int j=0;j<5;++j)edge_idx[i][j]=-1;
    int ei=0;for(auto e:edges){edge_idx[e.first][e.second]=edge_idx[e.second][e.first]=ei++;}
    for(int v=0;v<5;++v)for(int w=0;w<5;++w)if(w!=v)neigh[v].push_back(w);

    auto h0=full_profiles(0),h1=full_profiles(1);
    cout<<"unique_profiles H0="<<h0.size()<<" H1="<<h1.size()<<"\n";
    Spin init;init.fill(1);unordered_set<uint64_t> vacuum={enc_spin(init)};
    auto one=apply_support(vacuum,h0);block_stats(one,"after_H0");
    auto two=apply_support(one,h1);block_stats(two,"after_H1H0");

    bool pass=(h0.size()==252 && one.size()==1843 && two.size()==615884);
    cout<<"passed_regression="<<(pass?"true":"false")<<"\n";
    return pass?0:1;
}
