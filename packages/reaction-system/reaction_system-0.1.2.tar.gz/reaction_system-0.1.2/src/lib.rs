use pyo3::{prelude::*, exceptions::PyValueError};
use ::reaction_system::{ReactionSystem as RS, RsFunction as RF, Reaction, RsMinimize, EspressoError};

struct EspressoErrorPyO3(EspressoError);

impl From<EspressoErrorPyO3> for PyErr {
    fn from(error: EspressoErrorPyO3) -> Self {
        PyValueError::new_err(format!("{:?}", error.0))
    }
}

impl From<EspressoError> for EspressoErrorPyO3 {
    fn from(other: EspressoError) -> Self {
        Self(other)
    }
}


#[pyclass]
struct ReactionSystem (RS);

#[pymethods]
impl ReactionSystem {
  #[new]
  fn new(bg_size: usize) -> Self {
    ReactionSystem (RS::simple_new(bg_size))
  }

  /// adds a reaction to the reaction system
  fn push(&mut self, reactants: Vec<usize>, inhibitors: Vec<usize>, products: Vec<usize>) -> bool {
    self.0.push(Reaction { reactants, inhibitors, products })
  }

  fn remove(&mut self, reactants: Vec<usize>, inhibitors: Vec<usize>, products: Vec<usize>) {
    self.0.remove(Reaction { reactants, inhibitors, products })
  }

  fn result(&self, state: Vec<usize>) -> Vec<usize> {
    self.0.result(state).collect()
  }

  fn enabled(&self, state: Vec<usize>) -> bool {
    self.0.enabled(state)
  }

  fn degree(&self) -> usize {
    self.0.degree()
  }

  fn rank(&self) -> usize {
    self.0.rank()
  }

  fn minimize_rank(&self) -> Result<Self, EspressoErrorPyO3> {
    let rs = self.0.minimize_rank().map_err(|e| EspressoErrorPyO3::from(e))?;
    Ok(Self (rs))
  }

  fn minimize_rank_exact(&self) -> Result<Self, EspressoErrorPyO3> {
    let rs = self.0.minimize_rank_exact().map_err(|e| EspressoErrorPyO3::from(e))?;
    Ok(Self (rs))
  }

  fn minimize_degree(&self) -> Result<Self, EspressoErrorPyO3> {
    let rs = self.0.minimize_degree().map_err(|e| EspressoErrorPyO3::from(e))?;
    Ok(Self (rs))
  }

  fn complement(&self) -> Result<Self, EspressoErrorPyO3> {
    let rs = self.0.complement().map_err(|e| EspressoErrorPyO3::from(e))?;
    Ok(Self (rs))
  }

  fn primes(&self) -> Result<Self, EspressoErrorPyO3> {
    let rs = self.0.primes().map_err(|e| EspressoErrorPyO3::from(e))?;
    Ok(Self (rs))
  }

  fn essential_primes(&self) -> Result<Self, EspressoErrorPyO3> {
    let rs = self.0.essential_primes().map_err(|e| EspressoErrorPyO3::from(e))?;
    Ok(Self (rs))
  }

  fn __str__(&self) -> String {
    format!("{}", self.0)
  }
}

#[pyclass]
struct RsFunction (RF);

#[pymethods]
impl RsFunction {
  #[new]
  fn new(bg_size: usize) -> Self {
    Self (RF::simple_new(bg_size))
  }

  fn add(&mut self, input: Vec<usize>, output: Vec<usize>) -> Option<Vec<usize>> {
    self.0.add(input, output)
  }

  fn remove(&mut self, input: Vec<usize>) -> Option<Vec<usize>> {
    self.0.remove(input)
  }

  fn minimize_rank(&self) -> Result<ReactionSystem, EspressoErrorPyO3> {
    let rs = self.0.minimize_rank().map_err(|e| EspressoErrorPyO3::from(e))?;
    Ok(ReactionSystem (rs))
  }

  fn minimize_rank_exact(&self) -> Result<ReactionSystem, EspressoErrorPyO3> {
    let rs = self.0.minimize_rank_exact().map_err(|e| EspressoErrorPyO3::from(e))?;
    Ok(ReactionSystem (rs))
  }

  fn minimize_degree(&self) -> Result<ReactionSystem, EspressoErrorPyO3> {
    let rs = self.0.minimize_degree().map_err(|e| EspressoErrorPyO3::from(e))?;
    Ok(ReactionSystem (rs))
  }

  fn complement(&self) -> Result<ReactionSystem, EspressoErrorPyO3> {
    let rs = self.0.complement().map_err(|e| EspressoErrorPyO3::from(e))?;
    Ok(ReactionSystem (rs))
  }

  fn primes(&self) -> Result<ReactionSystem, EspressoErrorPyO3> {
    let rs = self.0.primes().map_err(|e| EspressoErrorPyO3::from(e))?;
    Ok(ReactionSystem (rs))
  }

  fn essential_primes(&self) -> Result<ReactionSystem, EspressoErrorPyO3> {
    let rs = self.0.essential_primes().map_err(|e| EspressoErrorPyO3::from(e))?;
    Ok(ReactionSystem (rs))
  }

  fn __str__(&self) -> String {
    format!("{}", self.0)
  }
}


/// A Python module implemented in Rust.
#[pymodule]
fn reaction_system(_py: Python, m: &PyModule) -> PyResult<()> {
  m.add_class::<ReactionSystem>()?;
  m.add_class::<RsFunction>()?;
  Ok(())
}
