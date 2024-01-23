struct User {
    name: String,
    email: String,
}

impl User {
    fn new(name: &str) -> User {
        User {
            name: name.to_string(),
            email: format!("{}@example.com", name.to_lowercase()),
        }
    }
}

fn main() {
    let user = User::new("Rishi");
    println!("{} <{}>", user.name, user.email);
}