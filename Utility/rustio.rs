use std::io;

fn main() {
    let vec: Vec<i32> = read_int_vec();

    for num in vec {
        println!("{}", num);
    }
}

fn read_int_vec() -> Vec<i32> {
    let mut line = String::new();
    io::stdin().read_line(&mut line).expect("input");
    let nums = line.trim().split(' ').flat_map(str::parse::<i32>).collect::<Vec<_>>();

    return nums;
}

fn read_string() -> String {
    let mut temp = String::new();
    io::stdin().read_line(&mut temp).expect("Failed to read String");

    return temp
}

fn read_int() -> i32 {
    let mut temp = String::new();
    io::stdin().read_line(&mut temp).expect("Failed to read String");
    let ret: i32 = temp.trim().parse().expect("Failed to parse");

    return ret;
}

fn read_long() -> i64 {
    let mut temp = String::new();
    io::stdin().read_line(&mut temp).expect("Failed to read String");
    let ret: i64 = temp.trim().parse().expect("Failed to parse");

    return ret;
}