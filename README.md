# CCTV Camera Live Streaming
Các bước giải quyết bài toán:
1. Lưu frames thành các chunks nhỏ, sau đó ghép lại thành video với codec **MPEG**.
2. Hiển thị video live trên website.
  
Chi tiết các bước được trình bày bên dưới.

## Tạo video với codec MPEG
Sử dụng thư viện **vidgear** để nhận các frame từ CCTV camera, sau đó lưu các frame
thành các chunk có định dạng là **.ts**, rồi ghép lại video với định dạng là **.m3u8**.  
Việc tách thành các chunk giúp ta có thể xem lại thời gian trong quá khứ tùy thuộc vào 
số lượng các chunk, nhưng việc tạo thành quá nhiều chunk sẽ tăng độ trễ.

## Hiển thị video live trên website
Tạo website sử dụng thư viện **Flask** trình chiếu video sau cùng, video này sẽ tự động 
sử dụng các chunk gần nhất để trình chiếu.

## Tham khảo
1. HLS video streaming website: https://github.com/susmitgaikwad/HLS-Streaming
2. Thư viện **VidGear**: https://github.com/abhiTronix/vidgear