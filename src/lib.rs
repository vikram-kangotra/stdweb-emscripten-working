use stdweb::js;
use stdweb::console;
use stdweb::web::alert;

#[no_mangle]
pub extern "C" fn run() {

    let greetings_from_js = js! {
        return "Hello Rust. I'm JavaScript!";
    };

    console!(log, "Hello JavaScript. I'm Rust!");

    alert(&greetings_from_js.into_string().unwrap());
}
