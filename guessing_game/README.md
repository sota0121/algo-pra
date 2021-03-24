# guessing game

document is [here](https://doc.rust-jp.rs/book-ja/ch02-00-guessing-game-tutorial.html).

## 予想を処理する

section is [here](https://doc.rust-jp.rs/book-ja/ch02-00-guessing-game-tutorial.html#%E4%BA%88%E6%83%B3%E3%82%92%E5%87%A6%E7%90%86%E3%81%99%E3%82%8B).

```rust
use std::io;

fn main() {
    println!("Guess the number!");          // 数を当ててごらん

    println!("Please input your guess.");   // ほら、予想を入力してね

    let mut guess = String::new();

    io::stdin().read_line(&mut guess)
        .expect("Failed to read line");     // 行の読み込みに失敗しました

    println!("You guessed: {}", guess);     // 次のように予想しました: {}
}
```

### point

- `use std::io;`
  - おそらく、`#include <iostream>` 的なものと予想
  - 違ったっぽい。どうも `using std` に近そうだ。もし、この文がない場合は、`io::stdin` が `std::io:stdin` になるらしい
- 標準入力をうけとる、文字列変数の宣言。Rustのデフォルトはイミュータブルなので、可変にするには、mutを明示的に書く
  - `let mut guess = String::new();`
  - Stringクラスの静的メソッドnew()を呼び出している。ここは、C++と同じ。
- `read_line(&mut guess)` について
  - read_lineは、「標準入力を取得し、引数に設定する」関数である
  - read_lineの第一引数は、「**参照**」かつ「**可変**」でなければならない。
  - 参照として、`&` を使う。（ここはC++と一緒）、出力引数なので、`mut` も書く。
  - 結果として、`(&mut guess)`
- `.expect()` のとこどうなってんだ？
  - 直感的には、read_lineの戻り値を判定して、その結果がエラーなら実行される場所っぽいが
  - どうやらメソッドチェインニングらしい。
  - つまり、`readline().expect()` なのだが、長くなるので改行しているとのこと
- `read_line()の戻り値はResult型`
  - Result型は頻出らしい。その実体は列挙子。つまりenum
  - 中身は、OkとErr（それぞれに数が付与されているだろうが、それを気にしなくて良い作りになっている）
  - `expect()` は、Result型のメソッドで、値がErrの場合、プログラムをクラッシュさせる、という役割を持つ
  - もし、Result型を返しているにも関わらず`expect()`を呼んでいないならば、コンパイル時にワーニングが出るらしい（ありがたい）
- 標準出力関数（マクロ）の書式指定
  - `println!("val {} is not val {}", x, y)`
  - 間隔的には、Pythonに等しい。


## ランダムな秘密の数字を生成する

section is [here](https://doc.rust-jp.rs/book-ja/ch02-00-guessing-game-tutorial.html#%E7%A7%98%E5%AF%86%E3%81%AE%E6%95%B0%E5%AD%97%E3%82%92%E7%94%9F%E6%88%90%E3%81%99%E3%82%8B).



### point

- 用語
  - パッケージのことをクレートと呼んでいる。
  - これからrandクレートを追加して、使うことになる。
  - 今作っている `guessing-game` は、**バイナリクレート**。randは、**ライブラリクレート**と呼ぶ
- 新しくライブラリパッケージ（クレート）を追加したいと思ったら
  - `Cargo.toml > [dependencies]` 直下に追加していく `rand = "0.3.14"` ってな感じで。
