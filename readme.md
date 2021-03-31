# algorithm

``` markdown
### 에라토스테네스의 체 

배열을 이용하여 소수를 구하는 알고리즘

`date: 2021-03-31`
```
``` javascript
const max = 200;
const arr = [];
const list = [];
for(let index=2; index<=max; index++){
    if( !!arr[index] === false ){
        list.push(index);
        for(let depth=index<<1; depth<=max; depth+=index){
            arr[depth] = true;
        }
    }
}
console.log(list);
```

시간복잡도도 공부해야 함.

