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
  - またまた違ったっぽい。どうやら、C++でいうと、`include` 兼 `using` と言ったところ。Pythonでいうと、`import` に該当する。ライブラリも読み込むし、名前空間の宣言もする感じ。
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
- `cargo doc --open`
  - ローカルに存在する全てのクレートのドキュメントをビルドし、ブラウザで閲覧できる機能。やばい。


## 秘密の数字と予想結果を比較する

section is [here](https://doc.rust-jp.rs/book-ja/ch02-00-guessing-game-tutorial.html#%E4%BA%88%E6%83%B3%E3%81%A8%E7%A7%98%E5%AF%86%E3%81%AE%E6%95%B0%E5%AD%97%E3%82%92%E6%AF%94%E8%BC%83%E3%81%99%E3%82%8B).


### point

- `use std::cmp::Ordering;`
  - cmp::OrderingもResultと同様に、列挙子であり。値は、Less, Greater, Equal
  - match式は複数のアーム（腕、パターン）を持つ。switchに近い存在か？
  - guessは、標準入力を受け取るために文字列で生成したが、ここから数値に変換しないと、matchで、secret_number と比較することができない。
  - 値を型変換する時によく使われるのが、シャドーイングというRust特有の機能だ。

```rust
let guess: u32 = guess.trim().parse()
    .expect("Please type a number!");
```

- このとき、右辺のguess（文字列）を左辺のguess（数値）で覆い隠す（シャドーイング）ことができる。何が嬉しいかというと、`guess_str` と `guess` などを作らなくて良くなること。
- `trim()` は文字列型のメソッドで、両端の空白を取り除く
- `parse()` も文字列型のメソッドで、数値に変換する。ただし、明示的に変換後の数値型を指定する必要がある。それが、左辺の`u32`である


## ループで複数回の予想を可能にする

section is [here](https://doc.rust-jp.rs/book-ja/ch02-00-guessing-game-tutorial.html#%E3%83%AB%E3%83%BC%E3%83%97%E3%81%A7%E8%A4%87%E6%95%B0%E5%9B%9E%E3%81%AE%E4%BA%88%E6%83%B3%E3%82%92%E5%8F%AF%E8%83%BD%E3%81%AB%E3%81%99%E3%82%8B).


### point

- while文みたいな役割を担うのが、`loop`
- match内の各アームでは、`=>` のあとに `{}` ブロックを作れる。その中でbreakを記述する。switch文ぽい。
- 「不正な場合クラッシュ」は`[Result].expect()` 、これを「適切なエラー処理」に変更する場合は、`match .. {Ok=>, Err=>}` を使う。ちょうど以下のように。

```rust
// 数値じゃなければクラッシュ
let guess: u32 = guess.trim().parse()
    .expect("Please type a number!");

// 戻り値によって適切なエラー処理
let guess: u32 = match guess.trim().parse() {
    Ok(num) => num, // num にparse結果の数値が入っている。それが guess: u32 に入れられる
    Err(_) => continue, // _ は、全てのエラーを指す
};
```

- 