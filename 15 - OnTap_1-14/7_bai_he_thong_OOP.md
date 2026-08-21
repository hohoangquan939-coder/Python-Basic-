# BỘ 7 BÀI TẬP HỆ THỐNG LỚN — ÁP DỤNG OOP TOÀN DIỆN
### Mỗi bài là 1 hệ thống nhiều class, dùng kiến thức Bài 1-14. Mỗi ngày làm 1 bài.

**Quy tắc chung cho cả 7 bài:**
- Bắt buộc có ít nhất 1 abstract class (`ABC` + `abstractmethod`)
- Bắt buộc có ít nhất 2 cấp kế thừa (class cha → class con → class cháu, hoặc nhiều class con cùng cha)
- Bắt buộc có ít nhất 1 thuộc tính private (`__`) với getter/setter
- Bắt buộc dùng polymorphism (vòng `for` gọi method chung trên list nhiều loại object khác nhau)
- Phải có xử lý lỗi bằng `try/except` ở phần nhập liệu
- Phải có chức năng ghi/đọc file để lưu dữ liệu

---

## Bài hệ thống 1 — Quản lý Sở thú (Zoo Management)

**Yêu cầu thiết kế:**

1. **Abstract class `Animal`:**
   - Thuộc tính: `name`, `age`, `__food_amount` (private — lượng thức ăn mỗi ngày, đơn vị kg)
   - Abstract method: `phat_am_thanh(self)` — mỗi loài kêu khác nhau
   - Abstract method: `loai_thuc_an(self)` — trả về `"Thit"` hoặc `"Thuc vat"`
   - Method thường: `get_food_amount(self)` / `set_food_amount(self, amount)` — setter phải kiểm tra `amount > 0`, nếu không in lỗi và không cho sửa
   - Method thường: `thong_tin(self)` — in ra `"{name} ({age} tuoi) - An: {food_amount}kg {loai_thuc_an} moi ngay"`

2. **Class con kế thừa `Animal`:** `Lion`, `Elephant`, `Monkey` (tối thiểu 3 loài)
   - Mỗi loài override `phat_am_thanh()` và `loai_thuc_an()` riêng
   - `Lion` thêm thuộc tính riêng `pride_size` (số lượng đàn)
   - `Elephant` thêm thuộc tính riêng `trunk_length`
   - `Monkey` thêm method riêng `leo_cay(self)` in ra `"{name} dang leo cay"`

3. **Class `Zoo` (sở thú) — quản lý tổng:**
   - Thuộc tính: `name`, `__animals` (list private chứa các object Animal)
   - `them_dong_vat(self, animal)` — thêm vào `__animals`
   - `tong_thuc_an_can_thiet(self)` — tính tổng kg thức ăn cần cho cả sở thú/ngày (dùng vòng `for` gọi `get_food_amount()` từng con — polymorphism)
   - `danh_sach_theo_loai_thuc_an(self, loai)` — trả về list tên các con vật ăn đúng loại thức ăn chỉ định (`"Thit"` hoặc `"Thuc vat"`)
   - `cho_tat_ca_keu(self)` — duyệt qua `__animals`, gọi `phat_am_thanh()` từng con (polymorphism)
   - `luu_file(self, filename)` — ghi thông tin toàn bộ sở thú ra file (tên, tuổi, loại thức ăn, lượng ăn)
   - `doc_file(self, filename)` — đọc file vừa ghi, in ra màn hình, có xử lý lỗi nếu file không tồn tại (`try/except FileNotFoundError`)

4. **Chương trình chính (main):**
   - Nhập từ bàn phím: tên sở thú, sau đó nhập liên tục thông tin từng con vật (loại, tên, tuổi, lượng ăn) cho đến khi gõ `"end"`
   - Xử lý lỗi nếu nhập tuổi hoặc lượng ăn không phải số (`try/except ValueError`), yêu cầu nhập lại
   - Sau khi nhập xong, in: tổng thức ăn cần thiết/ngày, danh sách con vật ăn thịt, cho tất cả kêu lên, lưu vào file `zoo_data.txt`

**Input mẫu:**
```
Nhap ten so thu: Saigon Zoo
Chon loai (lion/elephant/monkey/end): lion
Nhap ten: Simba
Nhap tuoi: 5
Nhap luong an (kg): 8
Nhap so luong day: 3
Chon loai (lion/elephant/monkey/end): monkey
Nhap ten: Kong
Nhap tuoi: 3
Nhap luong an (kg): 2
Chon loai (lion/elephant/monkey/end): end
```

**Output mẫu:**
```
Tong thuc an can thiet: 10kg/ngay
Dong vat an thit: ['Simba']
Simba: Gaaaau!
Kong: Khe khe!
Da luu vao file zoo_data.txt
```

---

## Bài hệ thống 2 — Quản lý Phương tiện Giao thông (Vehicle Rental)

**Yêu cầu thiết kế:**

1. **Abstract class `Vehicle`:**
   - Thuộc tính: `brand`, `model`, `__rental_price_per_day` (private)
   - Abstract method: `tinh_phi_thue(self, days)` — công thức tính phí khác nhau theo loại xe
   - Abstract method: `loai_xe(self)` — trả về tên loại (`"Xe may"`, `"O to"`, `"Xe tai"`)
   - Getter/setter cho `rental_price_per_day` (setter không cho giá âm)
   - Method `thong_tin(self)` in ra `"{brand} {model} - {loai_xe()} - {gia}/ngay"`

2. **Class con:** `Motorbike`, `Car`, `Truck` (kế thừa `Vehicle`)
   - `Motorbike`: `tinh_phi_thue` = `gia * days` (không phụ phí)
   - `Car`: thêm thuộc tính `num_seats`; `tinh_phi_thue` = `gia * days`, nếu `days >= 7` giảm 10% tổng
   - `Truck`: thêm thuộc tính `max_load_kg`; `tinh_phi_thue` = `gia * days + 200000` (phụ phí cố định)

3. **Class `RentalStore` (cửa hàng cho thuê):**
   - `__vehicles` (private list)
   - `them_xe(self, vehicle)`
   - `tim_xe_theo_loai(self, loai)` — trả về list các xe đúng loại (dùng `isinstance` hoặc gọi `loai_xe()`)
   - `xe_re_nhat(self)` — tìm xe có giá thuê/ngày thấp nhất (không dùng `min()` có sẵn)
   - `tinh_tong_doanh_thu(self, danh_sach_thue)` — nhận vào list các tuple `(vehicle, days)`, tính tổng tiền toàn bộ (polymorphism qua `tinh_phi_thue`)
   - `luu_danh_sach_xe(self, filename)` / `doc_danh_sach_xe(self, filename)` — ghi/đọc file

4. **Chương trình chính:**
   - Nhập liên tục thông tin xe (loại, brand, model, giá/ngày, thuộc tính riêng) đến khi gõ `"end"`
   - Xử lý lỗi nhập giá không phải số
   - Cho người dùng nhập 1 đơn thuê: chọn xe theo brand, nhập số ngày thuê, tính phí (xử lý lỗi nếu nhập số ngày <= 0 — dùng `raise Exception` tự tạo lỗi rồi `except` bắt lại)
   - In hoá đơn thuê xe, lưu danh sách xe vào file

**Lưu ý kỹ thuật mới:** Bài này yêu cầu thử dùng `raise Exception("...")` để tự tạo lỗi khi số ngày thuê <= 0, rồi dùng `except Exception as e:` để bắt và in `str(e)`.

---

## Bài hệ thống 3 — Hệ thống Trường học (School Management)

**Yêu cầu thiết kế:**

1. **Abstract class `Person`:**
   - Thuộc tính: `name`, `age`, `__id` (private, mã định danh)
   - Abstract method: `vai_tro(self)` — trả về `"Hoc sinh"` hoặc `"Giao vien"`
   - Getter `get_id()`

2. **Class `Student(Person)`:**
   - Thêm `__scores` (private dict — môn học: điểm)
   
   - `them_diem(self, mon, diem)` — kiểm tra `0 <= diem <= 10`, nếu sai in lỗi không cho thêm
   - `diem_trung_binh(self)` — tính trung bình toàn bộ `__scores`
   - `xep_loai(self)` — dựa trên điểm trung bình

   - Override `vai_tro()` → `"Hoc sinh"`

3. **Class `Teacher(Person)`:**
   - Thêm `subject` (môn dạy), `__students` (private list các Student mà giáo viên này phụ trách)
   - `them_hoc_sinh_phu_trach(self, student)`
   - `diem_trung_binh_lop(self)` — tính điểm TB của tất cả học sinh mình phụ trách (gọi `diem_trung_binh()` của từng Student — polymorphism)
   - Override `vai_tro()` → `"Giao vien"`

4. **Class `School` (quản lý tổng):**
   - `__people` (private list chứa cả Student và Teacher lẫn lộn)
   - `them_nguoi(self, person)`
   - `liet_ke_theo_vai_tro(self, vai_tro)` — trả về list tên người theo `vai_tro()` (dùng polymorphism, không dùng `isinstance`)
   - `hoc_sinh_gioi_nhat(self)` — tìm học sinh có điểm TB cao nhất trong toàn trường (cần lọc ra đúng Student trước, dùng `isinstance`)
   - `xuat_bao_cao(self, filename)` — ghi toàn bộ thông tin trường ra file, định dạng rõ ràng theo từng vai trò
   - `doc_bao_cao(self, filename)` — đọc lại, xử lý lỗi file không tồn tại

5. **Chương trình chính:**
   - Tạo 1 trường, nhập liên tục giáo viên và học sinh (xử lý lỗi nhập tuổi/điểm sai kiểu)
   - Với mỗi học sinh, nhập điểm tối thiểu 2 môn
   - Gán học sinh vào giáo viên phụ trách
   - In báo cáo: học sinh giỏi nhất, điểm TB từng lớp theo giáo viên, lưu file

---

## Bài hệ thống 4 — Hệ thống Đặt món Nhà hàng (Restaurant Order System)

**Yêu cầu thiết kế:**

1. **Abstract class `MenuItem`:**
   - Thuộc tính: `name`, `__base_price` (private)
   - Abstract method: `tinh_gia(self)` — công thức tính giá khác nhau
   - Abstract method: `mo_ta(self)` — trả về chuỗi mô tả món
   - Getter/setter giá (không cho giá âm)

2. **Class con:** `FoodItem`, `DrinkItem`, `ComboItem` (kế thừa `MenuItem`)
   - `FoodItem`: thêm `is_spicy` (bool); `tinh_gia()` = giá gốc, nếu cay thì `+5000`
   - `DrinkItem`: thêm `size` (`"S"`, `"M"`, `"L"`); `tinh_gia()` — size M = giá gốc, S = giá gốc - 5000, L = giá gốc + 10000
   - `ComboItem`: chứa **list các `MenuItem` khác** (kế thừa nhưng cũng chứa quan hệ "has-many" — đây gọi là **Composition**, khái niệm mới); `tinh_gia()` = tổng giá các món trong combo, giảm 15%

3. **Class `Order` (1 đơn hàng):**
   - `__items` (private list các MenuItem đã chọn)
   - `them_mon(self, item)`
   - `tinh_tong_tien(self)` — polymorphism qua `tinh_gia()`
   - `in_hoa_don(self)` — in từng món + giá + tổng cuối, dùng `mo_ta()` polymorphism

4. **Class `Restaurant`:**
   - `__menu` (private list toàn bộ MenuItem có trong quán)
   - `them_vao_menu(self, item)`
   - `tim_mon_theo_ten(self, name)` — trả về object MenuItem hoặc `None` nếu không có
   - `tao_don_hang(self)` — trả về object `Order` mới
   - `luu_menu(self, filename)` / `doc_menu(self, filename)`

5. **Chương trình chính:**
   - Tạo menu với ít nhất 5 món (đủ 3 loại), nhập từ bàn phím, xử lý lỗi giá nhập sai
   - Tạo 1 combo gồm 2-3 món có sẵn trong menu
   - Tạo đơn hàng, cho người dùng chọn món theo tên (gõ `"done"` để kết thúc chọn), xử lý lỗi nếu chọn tên món không tồn tại trong menu (không crash, yêu cầu chọn lại)
   - In hoá đơn cuối, lưu menu vào file

**Khái niệm mới cần tự tìm hiểu:** Composition (1 class chứa list các object của class khác) khác Inheritance ở điểm nào — tự suy nghĩ rồi mình sẽ hỏi lại.

---

## Bài hệ thống 5 — Hệ thống Ngân hàng (Banking System) — nâng cấp

**Yêu cầu thiết kế:**

1. **Abstract class `Account`:**
   - Thuộc tính: `owner`, `__balance` (private), `account_number`
   - Abstract method: `tinh_lai_suat(self)` — lãi suất khác nhau theo loại tài khoản
   - Method thường: `nap_tien(self, amount)`, `rut_tien(self, amount)` — đều kiểm tra `amount > 0`, `rut_tien` kiểm tra thêm không vượt quá `__balance`
   - Getter `get_balance()`
   - Method `ap_dung_lai_suat(self)` — cộng thêm `balance * tinh_lai_suat()` vào balance

2. **Class con:** `SavingsAccount`, `CheckingAccount` (kế thừa `Account`)
   - `SavingsAccount`: lãi suất cố định `0.05` (5%), nhưng **chỉ được rút tối đa 2 lần/tháng** (đếm số lần rút bằng thuộc tính riêng `__withdraw_count`, vượt quá thì báo lỗi không cho rút — dùng `raise Exception`)

   - `CheckingAccount`: lãi suất `0.01` (1%), nhưng cho phép `rut_tien` âm tối đa `-500000` (thấu chi/overdraft) — nghĩa là điều kiện kiểm tra rút tiền khác `SavingsAccount`

3. **Class `Bank`:**
   - `__accounts` (private list)
   - `mo_tai_khoan(self, account)`
   - `tong_tien_toan_bank(self)` — polymorphism qua `get_balance()`
   - `ap_dung_lai_suat_toan_bank(self)` — gọi `ap_dung_lai_suat()` cho từng account (polymorphism)
   - `tim_theo_so_tai_khoan(self, number)`
   - `sao_luu(self, filename)` / `phuc_hoi(self, filename)` — ghi/đọc file (định dạng tuỳ chọn nhưng phải đọc lại đúng)

4. **Chương trình chính:**
   - Mở 3-4 tài khoản (cả 2 loại), nhập từ bàn phím, validate số dư ban đầu không âm
   - Thực hiện 1 số giao dịch nạp/rút trên từng tài khoản, bắt lỗi rút quá số lần / quá hạn mức bằng `try/except`
   - Áp dụng lãi suất toàn bank, in tổng tiền trước/sau khi áp dụng lãi suất
   - Sao lưu ra file

---

# BÀI 15.6 — Game RPG (Turn-based Battle System)

## Yêu cầu thiết kế

### 1. Abstract class `Character`
- Thuộc tính: `name`, `_hp`, `_max_hp`, `attack_power` (dùng `_` để class con truy cập được)
- Abstract method: `ky_nang_dac_biet(self, target)` — mỗi loại nhân vật có kỹ năng riêng
- Method `tan_cong(self, target)` — gây `attack_power` damage lên `target`, gọi `target.nhan_damage(amount)`
- Method `nhan_damage(self, amount)` — trừ `_hp`, không cho xuống dưới `0`
- Method `hoi_mau(self, amount)` — cộng `_hp`, không cho vượt `_max_hp`
- Method `con_song(self)` — return `True` nếu `_hp > 0`
- Method `get_hp(self)` — return `_hp`
- Method `thong_tin(self)` — in `"{name} | HP: {_hp}/{_max_hp} | ATK: {attack_power}"`

### 2. Class con kế thừa `Character`

**`Warrior`:**
- `__init__(self, name)` — `_hp = _max_hp = 120`, `attack_power = 20`
- `ky_nang_dac_biet(self, target)` — gây `attack_power * 2` damage lên target, in `"{name} chém mạnh! Gây {damage} damage!"`

**`Mage`:**
- `__init__(self, name)` — `_hp = _max_hp = 80`, `attack_power = 35`
- `ky_nang_dac_biet(self, target)` — dùng `random.random()`:
  - 70% → gây `attack_power * 1.5` damage, in `"{name} tung phep! Gây {damage} damage!"`
  - 30% → phép trượt, gây 0 damage, in `"{name} tung phep nhung truot!"`

**`Healer`:**
- `__init__(self, name)` — `_hp = _max_hp = 90`, `attack_power = 10`
- `ky_nang_dac_biet(self, target)` — hồi máu `+30 hp` cho `target` (đồng minh), không vượt `_max_hp`, in `"{name} hoi mau cho {target.name}! +{amount} HP"`
- **Lưu ý:** `target` ở đây là **đồng minh**, không phải địch — người chơi tự chọn target từ team mình

### 3. Class `Battle`
- `__init__(self, team_a, team_b)` — `team_a` (list Character), `team_b` (list Character)
- `_log` (list private — lưu diễn biến từng lượt)
- `them_log(self, message)` — thêm chuỗi vào `_log` VÀ in ra màn hình luôn (không cần in 2 lần)
- `lay_song(self, team)` — trả về list các Character còn sống trong team (dùng `con_song()`)
- `kiem_tra_thang(self)` — return `"A"` nếu team_b thua, `"B"` nếu team_a thua, `None` nếu chưa ai thắng
- `luot_danh_cua_a(self)` — người chơi điều khiển:
  - Hiện danh sách nhân vật còn sống của team_a
  - Người chơi chọn **nhân vật tấn công** (nhập số thứ tự)
  - Nếu nhân vật là `Healer` và chọn kỹ năng đặc biệt → chọn target từ team_a
  - Nếu không phải Healer và chọn kỹ năng đặc biệt → chọn target từ team_b còn sống
  - Nếu chọn tấn công thường → chọn target từ team_b còn sống
  - Xử lý lỗi nếu nhập lựa chọn không hợp lệ (chỉ `1` hoặc `2`), yêu cầu nhập lại
- `luot_danh_cua_b(self)` — tự động:
  - Mỗi nhân vật còn sống của team_b **random** dùng tấn công thường hoặc kỹ năng đặc biệt (`random.choice([1, 2])`)
  - Target random từ team_a còn sống
- `bat_dau(self)` — vòng lặp chính:
  ```
  while True:
      luot_danh_cua_a()
      kiem_tra_thang() → nếu có kết quả thì break
      luot_danh_cua_b()
      kiem_tra_thang() → nếu có kết quả thì break
  ```
- `luu_log(self, filename)` — ghi toàn bộ `_log` ra file

### 4. Chương trình chính
- Dùng **data sẵn** — không nhập tay
- Tạo `team_a` gồm 3 nhân vật: 1 `Warrior("Quan")`, 1 `Mage("Nhi")`, 1 `Healer("Hung")`
- Tạo `team_b` gồm 3 quái: `Warrior("Quy Du")`, `Mage("Ma Phap Su")`, `Warrior("Troll")`
- Gọi `battle.bat_dau()`
- Sau khi kết thúc in ra team thắng, lưu log vào `battle_log.txt`

**Output mẫu mỗi lượt:**
```
=== LUOT CUA TEAM A ===
Con song: [Quan (HP:120), Nhi (HP:80), Hung (HP:90)]

Chon nhan vat tan cong:
1. Quan (Warrior) HP: 120
2. Nhi (Mage) HP: 80
3. Hung (Healer) HP: 90
Nhap lua chon (1-3): 1

Chon hanh dong:
1. Tan cong thuong (20 damage)
2. Ky nang dac biet (Chem manh - 40 damage)
Nhap lua chon (1-2): 2

Chon target:
1. Quy Du HP: 95
2. Ma Phap Su HP: 80
Nhap lua chon (1-2): 1

Quan chem manh! Gay 40 damage!
Quy Du con lai 80 HP

=== LUOT CUA TEAM B ===
Ma Phap Su tung phep! Gay 52 damage!
Quan con lai 68 HP
...
```

---

# BÀI 15.7 — Thư viện số (Digital Library)

## Yêu cầu thiết kế

### 1. Abstract class `Media`
- Thuộc tính: `title`, `author`, `_is_borrowed` (dùng `_`, không dùng `__` — lý do tương tự bài 15.6)
- `__init__` set `_is_borrowed = False` mặc định
- Abstract method: `thoi_gian_muon_toi_da(self)` — return số ngày tối đa (int)
- Abstract method: `phi_tre_han(self, days_late)` — return số tiền phạt (int)
- Abstract method: `loai(self)` — return tên loại (`"Sach"`, `"DVD"`, `"Tap chi"`)
- Method `muon(self)` — nếu `_is_borrowed == True` thì `raise Exception(f"{title} dang duoc muon!")`, ngược lại set `_is_borrowed = True`
- Method `tra(self)` — set `_is_borrowed = False`
- Method `dang_duoc_muon(self)` — return `_is_borrowed`
- Method `thong_tin(self)` — in `"{loai()} | {title} | {author} | {'Dang muon' if _is_borrowed else 'Con trong'}"`

### 2. Class con kế thừa `Media`

**`Book`:**
- `__init__(self, title, author, num_pages)` — thêm `num_pages`
- `thoi_gian_muon_toi_da()` → return `14`
- `phi_tre_han(days_late)` → return `days_late * 2000`
- `loai()` → return `"Sach"`

**`DVD`:**
- `__init__(self, title, author, duration_minutes)` — thêm `duration_minutes` (thời lượng phim)
- `thoi_gian_muon_toi_da()` → return `3`
- `phi_tre_han(days_late)` → return `days_late * 10000`
- `loai()` → return `"DVD"`

**`Magazine`:**
- `__init__(self, title, author, issue_number)` — thêm `issue_number` (số phát hành)
- `thoi_gian_muon_toi_da()` → return `7`
- `phi_tre_han(days_late)` → return `days_late * 5000`
- `loai()` → return `"Tap chi"`
- **Giới hạn riêng:** thêm `_borrow_count` (đếm tổng số lần đã mượn), override `muon()` — nếu `_borrow_count >= 2` thì `raise Exception(f"{title} da duoc muon 2 lan, khong the muon them!")`, ngược lại gọi `super().muon()` rồi tăng `_borrow_count += 1`

### 3. Class `Member`
- `__init__(self, name)` — `name`, `_borrowed_items` (list)
- `muon_media(self, media)`:
  - Gọi `media.muon()` trong `try/except Exception as e`
  - Nếu thành công → thêm `media` vào `_borrowed_items`, in `"{name} da muon: {media.title}"`
  - Nếu lỗi → in `str(e)`, không thêm vào list
- `tra_media(self, media)`:
  - Nếu `media` không có trong `_borrowed_items` → in `"{name} khong co muon {media.title}"`
  - Ngược lại → gọi `media.tra()`, xoá khỏi `_borrowed_items`, in `"{name} da tra: {media.title}"`
- `tinh_tong_phi_tre_han(self, ngay_tre_dict)`:
  - Nhận vào dict `{media: so_ngay_tre}` (ví dụ `{book1: 3, dvd1: 1}`)
  - Tính tổng phí bằng cách gọi `media.phi_tre_han(so_ngay_tre)` — polymorphism
  - Return tổng phí
- `thong_tin(self)` — in tên thành viên và danh sách đang mượn

### 4. Class `Library`
- `__init__(self, name)` — `name`, `_catalog` (list Media), `_members` (list Member)
- `them_media(self, media)` — thêm vào `_catalog`
- `them_thanh_vien(self, member)` — thêm vào `_members`
- `tim_media_con_trong(self)` — return list Media có `dang_duoc_muon() == False` (polymorphism)
- `thong_ke_theo_loai(self)` — return dict đếm số lượng từng loại:
  ```python
  # Dùng loai() — polymorphism, không cần isinstance
  # Output: {"Sach": 3, "DVD": 2, "Tap chi": 1}
  ```
- `xuat_bao_cao(self, filename)` — ghi ra file theo format:
  ```
  Thu vien: {name}
  ================
  SACH (3)
  - Harry Potter | J.K Rowling | Con trong
  - ...
  ================
  DVD (2)
  - ...
  ================
  TAP CHI (1)
  - ...
  ```
- `doc_bao_cao(self, filename)` — đọc lại, `try/except FileNotFoundError`

### 5. Chương trình chính (data sẵn, không nhập tay)

```python
def main():
    lib = Library("Thu Vien Trung Tam")

    # Tao media
    b1 = Book("Harry Potter", "J.K Rowling", 500)
    b2 = Book("Dac Nhan Tam", "Dale Carnegie", 320)
    b3 = Book("Clean Code", "Robert Martin", 431)
    d1 = DVD("Avengers", "Marvel", 180)
    d2 = DVD("Interstellar", "Nolan", 169)
    m1 = Magazine("Forbes", "Forbes Inc", 102)
    m2 = Magazine("National Geographic", "Nat Geo", 55)

    for media in [b1, b2, b3, d1, d2, m1, m2]:
        lib.them_media(media)

    # Tao thanh vien
    mem1 = Member("Quan")
    mem2 = Member("Nhi")
    mem3 = Member("Hung")

    for mem in [mem1, mem2, mem3]:
        lib.them_thanh_vien(mem)

    # Test muon/tra
    mem1.muon_media(b1)
    mem1.muon_media(d1)
    mem2.muon_media(b1)   # ← lỗi: b1 đang được mượn bởi mem1
    mem2.muon_media(m1)
    mem2.muon_media(m1)   # ← test Magazine borrow_count

    mem1.tra_media(b1)
    mem2.muon_media(b1)   # ← giờ mượn được vì mem1 đã trả

    # Test phi tre han
    ngay_tre = {d1: 2, b1: 0}
    phi = mem1.tinh_tong_phi_tre_han(ngay_tre)
    print(f"\nPhi tre han cua {mem1.name}: {phi} VND")

    # Thong ke
    print(f"\nThong ke theo loai: {lib.thong_ke_theo_loai()}")
    print(f"\nMedia con trong:")
    for media in lib.tim_media_con_trong():
        media.thong_tin()

    # Xuat bao cao
    lib.xuat_bao_cao("library_report.txt")
    lib.doc_bao_cao("library_report.txt")
```

**Lưu ý khi code:**
- Bài này không có gì kỹ thuật mới — tổng hợp lại toàn bộ OOP đã học
- Focus vào thiết kế class sạch, method rõ ràng, xử lý lỗi đúng chỗ
- `thong_ke_theo_loai()` dùng `loai()` (polymorphism) thay vì `isinstance` — đây là cách Pythonic hơn


