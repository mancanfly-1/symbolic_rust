#![no_std] // don't link the Rust standard library
#![no_main] // disable all Rust-level entry points

use core::panic::PanicInfo;
/// This function is called on panic.
#[panic_handler]
fn panic(_info: &PanicInfo) -> ! {
    loop {}
}

#[macro_use]
mod a;


// // #[no_mangle]
// fn inc()
// {
//     unsafe{AGE +=1;}
//     // print!("{:?}", AGE)}
// }

#[no_mangle]
pub extern "C" fn rust_main() -> ! {
    loop{}
}

