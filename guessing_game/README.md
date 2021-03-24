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

