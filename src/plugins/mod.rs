pub(crate) mod url_sanitize;
pub(crate) mod decoders;

use serde_json;

pub trait Plugin {
  const NAME: &'static str;
  fn new() -> Self;
  fn perform_lookup(&self, value: &str) -> Result<serde_json::Value, String>;
  fn run(&self);
  fn get_name(&self) -> &str {
    return Self::NAME;
  }
}