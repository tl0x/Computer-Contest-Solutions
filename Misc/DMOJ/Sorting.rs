use std::io;

fn main() {
    let n = read_int();

    let mut vec: Vec<i32> = Vec::new();

    for i in 0..n {
        vec.push(read_int());
    }
    vec.sort();

    for x in vec {
        println!("{}", x);
    }
}

fn read_int() -> i32 {
    let mut temp = String::new();
    io::stdin().read_line(&mut temp).expect("Failed to read String");
    let ret: i32 = temp.trim().parse().expect("Failed to parse");

    return ret;
}