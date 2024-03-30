# TWPaws工具組後端


## API清單

### 忠誠點數類:

#### 取得忠誠點數清單
- `GET /api/redemption/rewards`
- Response: 同Twitch API回傳內容

#### 取得特定忠誠點數已兌換名單
- `GET /api/redemption/rewards-redemption`
- Parameters
  | Name         | Type   | Required |
  | ------------ | ------ | -------- |
  | rewardID     | string | yes      |
- Response: 同Twitch API回傳內容

#### 創建忠誠點數
- `POST /api/redemption/rewards`
- Body (JSON)
  | Name                                  | Type    | Required |
  | ------------------------------------- | ------- | -------- |
  | title                                 | string  | yes      |
  | cost                                  | integer | yes      |
  | prompt                                | string  | no       |
  | is_enabled                            | boolean | no       |
  | background_color                      | string  | no       |
  | is_user_input_required                | boolean | no       |
  | is_max_per_stream_enabled             | boolean | no       |
  | max_per_stream                        | boolean | no       |
  | is_max_per_user_per_stream_enabled    | boolean | no       |
  | max_per_user_per_stream               | integer | no       |
  | is_global_cooldown_enabled            | boolean | no       |
  | global_cooldown_seconds               | integer | no       |
  | should_redemptions_skip_request_queue | boolean | no       |
- Response: 同Twitch API回傳內容

#### 刪除忠誠點數
- `DELETE /api/redemption/rewards/<rewardId>`
- Response: 同Twitch API回傳內容

#### 更新忠誠點數
- `PATCH /api/redemption/rewards/<rewardId>`
- Body(JSON)
  | Name                                  | Type    | Required |
  | ------------------------------------- | ------- | -------- |
  | title                                 | string  | yes      |
  | cost                                  | integer | yes      |
  | prompt                                | string  | no       |
  | is_enabled                            | boolean | no       |
  | background_color                      | string  | no       |
  | is_user_input_required                | boolean | no       |
  | is_max_per_stream_enabled             | boolean | no       |
  | max_per_stream                        | boolean | no       |
  | is_max_per_user_per_stream_enabled    | boolean | no       |
  | max_per_user_per_stream               | integer | no       |
  | is_global_cooldown_enabled            | boolean | no       |
  | global_cooldown_seconds               | integer | no       |
  | should_redemptions_skip_request_queue | boolean | no       |
- Response: 同Twitch API回傳內容

### 使用者相關:

#### 取得broadcaster id
- `GET /api/user/broadcasters`
- Response: 是否成功