# cargo basic commands

- debug binary build
  - `cargo build`
- debug binary run
  - `./target/debug/hello_cargo`
- debug binary build and run in 1 step
  - `cargo run`
- in case : release binary
  - `cargo build --release`
  - `cargo run --release`
- check if sources can be compiled and don't make binary
  - `cargo check`


## tips

- 開発中は、頻繁に `cargo check` でコンパイルできるかを確認（バイナリ生成しないので高速に動く）
- いざ、実行する段階になると、はじめて `cargo build` する