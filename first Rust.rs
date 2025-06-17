fn main() {
    println!("Hello, world!");

    let result = add(5, 7);
    println!("5 + 7 = {}", result);
}

fn add(x: i32, y: i32) -> i32 {
    x + y
}
