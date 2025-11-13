export enum RelationType {
  HAS = "имеет",
  IS_PART_OF = "является частью",
  CHARACTERIZES = "характеризует",
  PARTICIPATES_IN = "участвует в",
  INCLUDES = "включает в себя",
  CONTAINS = "вмещает в себя",
  IS_SUBTASK = "является подзадачей",
  IS_SUBPROPERTY = "является подсвойством",
  IS_PROPERTY = "имеет свойство",
  RELATED_TO = "связан с",
  USED_IN = "используется в",
  TRANSFORMS_TO = "преобразуется в",
  CREATES = "создает",
  IS_RESULT_OF = "является результатом",
  PRODUCES = "производит",
  RECOGNIZED_BY = "распознается через",
}

export interface Relation {
  target_term_id: string;
  relation_type: RelationType;
  description?: string;
}

export interface Term {
  id: string;
  term: string;
  definition: string;
  category?: string;
  relations: Relation[];
}

export interface TermsResponse {
  total: number;
  items: Term[];
}

export interface CategoryResponse {
  categories: string[];
}
