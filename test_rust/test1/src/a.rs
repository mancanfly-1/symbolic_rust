
#[no_mangle]
static mut AGE:u32 = 1;
#[no_mangle]
pub static Max:u32 = 12;
#[no_mangle]
pub extern fn add(x:u32, y:u32)->u32
{
    // unsafe
    // {
    //     if AGE < Max {
    //         AGE +=1;
    //     }
    // }
    x + y
}
// #[no_mangle]
// pub fn inc1()
// {
//     let mut x = 0;
//     x = 6;
// }

